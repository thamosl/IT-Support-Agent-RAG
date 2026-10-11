import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
from unittest.mock import patch

from langchain_core.documents import Document
from google.genai.errors import ClientError

from app.rag import workflow
from app.api import routes
import ingest_sample_kb


class FakeRetriever:
    def __init__(self, documents):
        self.documents = documents
        self.queries = []

    def invoke(self, query):
        self.queries.append(query)
        return self.documents


class FakeWebSearch:
    def __init__(self, result):
        self.result = result
        self.queries = []

    def invoke(self, query):
        self.queries.append(query["query"])
        return self.result


class FakeModel:
    def __init__(self, route="kb", kb_grades=None, web_grades=None, answers=None):
        self.route = route
        self.kb_grades = iter(kb_grades or ["weak"])
        self.web_grades = iter(web_grades or ["good"])
        self.answers = iter(answers or ["Test answer"])

    def with_structured_output(self, schema, method=None):
        if method not in (None, "json_mode"):
            raise ValueError(f"Unsupported structured-output method: {method}")
        if schema is workflow.RouteDecision:
            return SimpleNamespace(invoke=lambda _: schema(route=self.route))

        def grade(prompt):
            grades = self.web_grades if "Web evidence:" in prompt else self.kb_grades
            return schema(grade=next(grades, "weak"))

        return SimpleNamespace(invoke=grade)

    def invoke(self, prompt):
        if "Rewrite this IT support question" in prompt:
            return SimpleNamespace(content="rewritten support query")
        return SimpleNamespace(content=next(self.answers, "Test answer"))


class WorkflowTests(unittest.TestCase):
    def run_workflow(
        self,
        *,
        route="kb",
        documents=None,
        web_result=None,
        kb_grades=None,
        web_grades=None,
        answers=None,
        max_retries=1,
    ):
        model = FakeModel(route, kb_grades, web_grades, answers)
        retriever = FakeRetriever(documents or [])
        web_search = FakeWebSearch(web_result or {})
        with (
            patch.object(workflow, "llm", return_value=model),
            patch.object(workflow, "fallback_llm", return_value=None),
            patch.object(workflow, "get_retriever", return_value=retriever),
            patch.object(workflow, "web_search_tool", return_value=web_search),
            patch.object(workflow.settings, "max_retries", max_retries),
        ):
            result = workflow.ask_question("How do I solve this support issue?")
        return result, retriever, web_search

    def assert_nonempty_answer(self, result):
        self.assertIsInstance(result["answer"], str)
        self.assertTrue(result["answer"].strip())

    def test_direct_question_generates_answer_without_retrieval(self):
        result, retriever, web_search = self.run_workflow(route="direct")
        self.assertEqual(result["source_used"], "direct")
        self.assertEqual(retriever.queries, [])
        self.assertEqual(web_search.queries, [])
        self.assert_nonempty_answer(result)

    def test_sufficient_kb_evidence_generates_answer_and_citation(self):
        doc = Document(page_content="Reset steps", metadata={"source": "password-policy.md"})
        result, _, web_search = self.run_workflow(
            documents=[doc],
            kb_grades=["good"],
        )
        self.assertEqual(result["source_used"], "private_kb")
        self.assertEqual(result["citations"][0]["title"], "password-policy.md")
        self.assertEqual(web_search.queries, [])
        self.assert_nonempty_answer(result)

    def test_retrieval_skips_duplicate_vectors_and_keeps_distinct_sources(self):
        duplicate = Document(
            page_content="Existing handbook chunk",
            metadata={"source": "IT_Support_Handbook.md", "start_index": 120},
        )
        added_file = Document(
            page_content="New employee lifecycle guidance",
            metadata={"source": "10_Employee_Lifecycle.md", "start_index": 0},
        )
        retriever = FakeRetriever([duplicate, duplicate, added_file])
        with (
            patch.object(workflow, "get_retriever", return_value=retriever),
            patch.object(workflow.settings, "top_k", 2),
        ):
            result = workflow.retrieve_kb({
                "question": "How do I onboard a new employee?",
                "current_query": "How do I onboard a new employee?",
                "kb_docs": [],
                "web_results": "",
                "kb_grade": "",
                "web_grade": "",
                "answer": "",
                "source_used": "",
                "retry_count": 0,
                "trace": [],
                "citations": [],
            })
        self.assertEqual(result["kb_docs"], [duplicate, added_file])

    def test_sample_ingester_accumulates_documents_from_all_supported_files(self):
        with TemporaryDirectory() as temporary_directory:
            folder = Path(temporary_directory)
            first_file = folder / "first.md"
            second_file = folder / "second.md"
            first_file.touch()
            second_file.touch()
            first_doc = Document(page_content="First document", metadata={})
            second_doc = Document(page_content="Second document", metadata={})
            chunks = [first_doc, second_doc]
            settings = SimpleNamespace(sample_kb_dir=str(folder))
            with (
                patch.object(ingest_sample_kb, "get_settings", return_value=settings),
                patch.object(
                    ingest_sample_kb,
                    "load_file",
                    side_effect=[[first_doc], [second_doc]],
                ) as load_file,
                patch.object(
                    ingest_sample_kb,
                    "chunk_documents",
                    return_value=chunks,
                ) as chunk_documents,
                patch.object(
                    ingest_sample_kb,
                    "add_documents",
                    return_value=["first-id", "second-id"],
                ) as add_documents,
            ):
                ingest_sample_kb.main()

            self.assertEqual(load_file.call_count, 2)
            chunk_documents.assert_called_once_with([first_doc, second_doc])
            add_documents.assert_called_once_with(chunks)

    def test_weak_kb_evidence_falls_back_to_web_search(self):
        result, _, web_search = self.run_workflow(
            web_result={
                "answer": "External answer",
                "results": [{"title": "Vendor guide", "url": "https://example.com", "content": "Steps"}],
            },
            kb_grades=["weak"],
            web_grades=["good"],
        )
        self.assertEqual(result["source_used"], "web_search")
        self.assertEqual(len(web_search.queries), 1)
        self.assertEqual(result["citations"][0]["url"], "https://example.com")
        self.assert_nonempty_answer(result)

    def test_weak_web_evidence_rewrites_query_and_retries(self):
        result, retriever, web_search = self.run_workflow(
            web_result={"answer": "External answer"},
            kb_grades=["weak", "weak"],
            web_grades=["weak", "good"],
        )
        self.assertEqual(result["source_used"], "web_search")
        self.assertEqual(len(retriever.queries), 2)
        self.assertEqual(len(web_search.queries), 2)
        self.assertEqual(web_search.queries[1], "rewritten support query")
        self.assert_nonempty_answer(result)

    def test_weak_web_evidence_after_retry_returns_insufficient_message(self):
        result, _, web_search = self.run_workflow(
            web_result={"answer": "Unhelpful result"},
            kb_grades=["weak", "weak"],
            web_grades=["weak", "weak"],
        )
        self.assertEqual(result["source_used"], "insufficient_evidence")
        self.assertEqual(len(web_search.queries), 2)
        self.assert_nonempty_answer(result)

    def test_missing_kb_and_web_evidence_returns_insufficient_message(self):
        result, _, web_search = self.run_workflow(
            web_result={},
            kb_grades=["weak", "weak"],
            web_grades=["good", "good"],
        )
        self.assertEqual(result["source_used"], "insufficient_evidence")
        self.assertIn("no search results", " ".join(result["trace"]).lower())
        self.assertEqual(len(web_search.queries), 2)
        self.assert_nonempty_answer(result)

    def test_empty_generation_never_returns_blank_answer(self):
        for route, kb_grades, web_grades, documents, web_result in (
            ("direct", None, None, None, None),
            ("kb", ["good"], None, [Document(page_content="Relevant", metadata={})], None),
            ("kb", ["weak"], ["good"], None, {"answer": "Relevant web evidence"}),
        ):
            with self.subTest(source=route, kb_grades=kb_grades):
                result, _, _ = self.run_workflow(
                    route=route,
                    documents=documents,
                    web_result=web_result,
                    kb_grades=kb_grades,
                    web_grades=web_grades,
                    answers=["   "],
                )
                self.assertEqual(result["source_used"], "generation_error")
                self.assert_nonempty_answer(result)

    def test_empty_query_rewrite_retries_with_existing_query(self):
        class EmptyRewriteModel(FakeModel):
            def invoke(self, prompt):
                if "Rewrite this IT support question" in prompt:
                    return SimpleNamespace(content="  ")
                return SimpleNamespace(content="Test answer")

        model = EmptyRewriteModel(kb_grades=["weak", "weak"], web_grades=["weak", "good"])
        retriever = FakeRetriever([])
        web_search = FakeWebSearch({"answer": "Useful external result"})
        with (
            patch.object(workflow, "llm", return_value=model),
            patch.object(workflow, "get_retriever", return_value=retriever),
            patch.object(workflow, "web_search_tool", return_value=web_search),
            patch.object(workflow.settings, "max_retries", 1),
        ):
            result = workflow.ask_question("How do I solve this support issue?")
        self.assertEqual(result["source_used"], "web_search")
        self.assertEqual(web_search.queries[0], web_search.queries[1])
        self.assert_nonempty_answer(result)

    def test_chat_api_returns_answer_trace_and_citations(self):
        workflow_result = {
            "answer": "Verified answer",
            "source_used": "web_search",
            "trace": ["Web search", "Answer generation"],
            "citations": [{"title": "Vendor guide", "url": "https://example.com", "type": "web"}],
        }
        with (
            patch.object(routes, "ask_question", return_value=workflow_result),
            patch.object(routes, "write_audit"),
        ):
            response = routes.chat(routes.ChatRequest(question="How do I fix this?"))
        self.assertEqual(response["answer"], "Verified answer")
        self.assertEqual(response["trace"], workflow_result["trace"])
        self.assertEqual(response["citations"], workflow_result["citations"])

    def test_fallback_is_used_when_primary_invocation_fails(self):
        class Runnable:
            def __init__(self, should_fail):
                self.should_fail = should_fail

            def with_fallbacks(self, fallbacks):
                return FailoverRunnable(self, fallbacks)

            def invoke(self, prompt):
                self.last_prompt = prompt
                if self.should_fail:
                    raise RuntimeError("Primary provider unavailable")
                return SimpleNamespace(content="Fallback answer")

        class FailoverRunnable:
            def __init__(self, primary, fallbacks):
                self.primary = primary
                self.fallbacks = fallbacks

            def invoke(self, prompt):
                try:
                    return self.primary.invoke(prompt)
                except Exception:
                    for fallback in self.fallbacks:
                        return fallback.invoke(prompt)
                    raise

        with (
            patch.object(workflow, "llm", return_value=Runnable(should_fail=True)),
            patch.object(workflow, "fallback_llm", return_value=Runnable(should_fail=False)),
        ):
            response = workflow.invoke_llm("Generate an answer")
        self.assertEqual(response.content, "Fallback answer")

    def test_gemini_fallback_handles_groq_quota_exception(self):
        class Model:
            def __init__(self, error=None, response=None):
                self.error = error
                self.response = response
                self.calls = 0

            def invoke(self, prompt):
                self.last_prompt = prompt
                self.calls += 1
                if self.error is not None:
                    raise self.error
                return self.response

        primary = Model(error=ClientError(429, {"message": "quota exceeded"}))
        gemini = Model(response=SimpleNamespace(content="Gemini fallback answer"))
        with (
            patch.object(workflow, "llm", return_value=primary),
            patch.object(workflow, "fallback_llm", return_value=gemini),
            patch.object(workflow, "_primary_quota_exceeded", False),
        ):
            first = workflow.invoke_llm("First request")
            second = workflow.invoke_llm("Second request")

        self.assertEqual(first.content, "Gemini fallback answer")
        self.assertEqual(second.content, "Gemini fallback answer")
        self.assertEqual(primary.calls, 1)
        self.assertEqual(gemini.calls, 2)

    def test_quota_latch_routes_structured_calls_directly_to_gemini(self):
        class StructuredModel:
            def __init__(self, error=None, result=None):
                self.error = error
                self.result = result
                self.calls = 0

            def with_structured_output(self, schema, method):
                self.schema = schema
                self.method = method
                return self

            def invoke(self, prompt):
                self.last_prompt = prompt
                self.calls += 1
                if self.error is not None:
                    raise self.error
                return self.result

        primary = StructuredModel(
            error=ClientError(429, {"message": "RESOURCE_EXHAUSTED"})
        )
        expected = workflow.RouteDecision(route="direct")
        gemini = StructuredModel(result=expected)
        with (
            patch.object(workflow, "llm", return_value=primary),
            patch.object(workflow, "fallback_llm", return_value=gemini),
            patch.object(workflow, "_primary_quota_exceeded", False),
        ):
            first = workflow.structured_llm(workflow.RouteDecision, "json_mode").invoke("route")
            second = workflow.structured_llm(workflow.RouteDecision, "json_mode").invoke("route")

        self.assertEqual(first.route, "direct")
        self.assertEqual(second.route, "direct")
        self.assertEqual(primary.calls, 1)
        self.assertEqual(gemini.calls, 2)

    def test_fallback_is_used_when_structured_primary_fails(self):
        class StructuredRunnable:
            def __init__(self, fail, schema):
                self.fail = fail
                self.schema = schema

            def with_fallbacks(self, fallbacks):
                return FallbackRunnable(self, fallbacks)

            def invoke(self, prompt):
                self.last_prompt = prompt
                if self.fail:
                    raise RuntimeError("Primary structured output unavailable")
                if self.schema is workflow.RouteDecision:
                    return self.schema(route="direct")
                return self.schema(grade="good")

        class Model:
            def __init__(self, fail):
                self.fail = fail

            def with_structured_output(self, schema, method):
                if method != "json_mode":
                    raise ValueError(f"Unexpected structured-output method: {method}")
                return StructuredRunnable(self.fail, schema)

        class FallbackRunnable:
            def __init__(self, primary, fallbacks):
                self.primary = primary
                self.fallbacks = fallbacks

            def invoke(self, prompt):
                try:
                    return self.primary.invoke(prompt)
                except Exception:
                    return self.fallbacks[0].invoke(prompt)

        with (
            patch.object(workflow, "llm", return_value=Model(fail=True)),
            patch.object(workflow, "fallback_llm", return_value=Model(fail=False)),
        ):
            result = workflow.structured_llm(workflow.RouteDecision, "json_mode").invoke("route")
        self.assertEqual(result.route, "direct")

    def test_groq_is_primary_and_gemini_is_fallback(self):
        primary_model = object()
        fallback_model = object()
        with (
            patch.object(workflow.settings, "gemini_api_key", "gemini-test-key"),
            patch.object(workflow.settings, "groq_api_key", "groq-test-key"),
            patch.object(workflow, "_llm", None),
            patch.object(workflow, "_fallback_llm", None),
            patch.object(workflow, "_llm_provider", None),
            patch.object(workflow, "ChatGoogleGenerativeAI", return_value=fallback_model) as gemini,
            patch.object(workflow, "ChatGroq", return_value=primary_model) as groq,
        ):
            selected_primary = workflow.llm()
            selected_fallback = workflow.fallback_llm()
        self.assertIs(selected_primary, primary_model)
        self.assertIs(selected_fallback, fallback_model)
        gemini.assert_called_once()
        groq.assert_called_once()


if __name__ == "__main__":
    unittest.main()

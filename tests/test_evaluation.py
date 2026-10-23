import unittest
from types import SimpleNamespace
from unittest.mock import patch, MagicMock
from langchain_core.documents import Document

from app.rag.evaluation import (
    RAGEvaluation,
    ChunkEvaluation,
    fallback_evaluate,
    build_judge_prompt,
    extract_keywords,
)
from app.rag import workflow
from app.services import audit
from app.api import routes

class EvaluationTests(unittest.TestCase):
    def test_extract_keywords(self):
        text = "How do I reset my company VPN password for Windows?"
        keywords = extract_keywords(text)
        self.assertIn("reset", keywords)
        self.assertIn("company", keywords)
        self.assertIn("vpn", keywords)
        self.assertIn("password", keywords)
        self.assertIn("windows", keywords)
        self.assertNotIn("how", keywords)
        self.assertNotIn("the", keywords)

    def test_fallback_evaluate_direct_conversation(self):
        result = fallback_evaluate(
            question="Hello! Good morning.",
            chunks=[],
            answer="Good morning! How can I assist you with your IT needs today?",
            source="direct"
        )
        self.assertEqual(result.verdict, "PASS")
        self.assertEqual(result.context_relevance, 1.0)
        self.assertEqual(result.groundedness, 1.0)
        self.assertGreaterEqual(result.answer_relevance, 0.9)
        self.assertGreaterEqual(result.overall_score, 0.9)
        self.assertEqual(len(result.chunk_evaluations), 0)

    def test_fallback_evaluate_insufficient_evidence(self):
        result = fallback_evaluate(
            question="What is the internal code for secret project X?",
            chunks=[],
            answer="I couldn't find enough reliable evidence in the company knowledge base or external search.",
            source="insufficient_evidence"
        )
        self.assertEqual(result.verdict, "PASS")
        self.assertLessEqual(result.context_relevance, 0.5)
        self.assertEqual(result.groundedness, 1.0)
        self.assertGreaterEqual(result.answer_relevance, 0.8)

    def test_fallback_evaluate_with_relevant_chunks(self):
        chunks = [
            {
                "source": "vpn-guide.md",
                "content": "To connect to the corporate VPN, download Cisco AnyConnect and enter vpn.company.com."
            },
            {
                "source": "general-faq.md",
                "content": "Cafeteria lunch hours are 12:00 PM to 2:00 PM Monday through Friday."
            }
        ]
        question = "How do I connect to the corporate VPN?"
        answer = "To connect to the corporate VPN, install Cisco AnyConnect and use the server address vpn.company.com."
        
        result = fallback_evaluate(question, chunks, answer, source="private_kb")
        
        self.assertEqual(len(result.chunk_evaluations), 2)
        # First chunk should have high score
        self.assertTrue(result.chunk_evaluations[0].is_relevant)
        self.assertGreater(result.chunk_evaluations[0].score, 0.5)
        # Second chunk should be lower
        self.assertLess(result.chunk_evaluations[1].score, result.chunk_evaluations[0].score)
        # Groundedness and answer relevance should be high
        self.assertGreaterEqual(result.groundedness, 0.7)
        self.assertGreaterEqual(result.answer_relevance, 0.7)
        self.assertEqual(result.verdict, "PASS")

    def test_build_judge_prompt_structure(self):
        prompt = build_judge_prompt(
            question="My laptop won't turn on",
            chunks=[{"source": "hardware.md", "content": "Hold power button for 15 seconds."}],
            answer="Perform a hard reset by holding the power button for 15 seconds.",
            source="private_kb"
        )
        self.assertIn("Context Relevance", prompt)
        self.assertIn("Groundedness / Faithfulness", prompt)
        self.assertIn("Answer Relevancy", prompt)
        self.assertIn("hardware.md", prompt)
        self.assertIn("My laptop won't turn on", prompt)

    def test_workflow_evaluate_rag_node(self):
        state = {
            "question": "How to reset password?",
            "current_query": "How to reset password?",
            "kb_docs": [Document(page_content="Go to portal.company.com to reset password.", metadata={"source": "pwd.md"})],
            "web_results": "",
            "kb_grade": "good",
            "web_grade": "",
            "answer": "Visit portal.company.com and follow the reset password steps.",
            "source_used": "private_kb",
            "retry_count": 0,
            "trace": [],
            "citations": [],
            "evaluation": {}
        }
        
        result = workflow.evaluate_rag(state)
        self.assertIn("evaluation", result)
        eval_data = result["evaluation"]
        self.assertIn("context_relevance", eval_data)
        self.assertIn("groundedness", eval_data)
        self.assertIn("answer_relevance", eval_data)
        self.assertIn("overall_score", eval_data)
        self.assertIn("verdict", eval_data)
        self.assertIn("chunk_evaluations", eval_data)
        self.assertTrue(any("LLM Judge →" in t for t in result["trace"]))

    def test_audit_write_and_summary(self):
        sample_eval = {
            "overall_score": 0.95,
            "verdict": "PASS",
            "context_relevance": 0.92,
            "groundedness": 0.98,
            "answer_relevance": 0.95
        }
        audit.write_audit("Sample question", "private_kb", ["Trace 1"], sample_eval)
        recent = audit.get_recent_audits(limit=5)
        self.assertTrue(len(recent) > 0)
        first = recent[0]
        self.assertEqual(first["question"], "Sample question")
        self.assertEqual(first["evaluation"].get("verdict"), "PASS")
        
        summary = audit.get_evaluations_summary()
        self.assertGreater(summary["total_evaluated"], 0)
        self.assertGreater(summary["avg_overall_score"], 0.0)

    def test_api_routes_include_evaluation(self):
        mock_workflow_result = {
            "answer": "Test answer",
            "source_used": "private_kb",
            "trace": ["Trace A"],
            "citations": [],
            "evaluation": {
                "overall_score": 0.94,
                "verdict": "PASS",
                "context_relevance": 0.90,
                "groundedness": 0.96,
                "answer_relevance": 0.96,
                "critique": "Solid response."
            }
        }
        with patch.object(routes, "ask_question", return_value=mock_workflow_result):
            response = routes.chat(routes.ChatRequest(question="Test question?"))
            self.assertIn("evaluation", response)
            self.assertEqual(response["evaluation"]["verdict"], "PASS")
            self.assertEqual(response["evaluation"]["overall_score"], 0.94)

        activity_response = routes.get_activity(limit=10)
        self.assertIn("activities", activity_response)
        
        summary_response = routes.get_summary()
        self.assertIn("total_evaluated", summary_response)
        self.assertIn("avg_overall_score", summary_response)

if __name__ == "__main__":
    unittest.main()

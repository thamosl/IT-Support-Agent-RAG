import logging
import time
from typing import Literal
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnableLambda
from langchain_tavily import TavilySearch
from langgraph.graph import StateGraph, START, END
from app.core.config import get_settings
from app.rag.state import AgentState, RouteDecision, EvidenceGrade
from app.rag.vectorstore import get_retriever

logger = logging.getLogger(__name__)
settings = get_settings()

_llm = None
_fallback_llm = None
_llm_provider = None
_primary_quota_exceeded = False
_web_search = None

def llm():
    global _llm, _llm_provider
    if _llm is None:
        if settings.groq_api_key:
            _llm = ChatGroq(
                model=settings.groq_model,
                temperature=0,
                api_key=settings.groq_api_key,
            )
            _llm_provider = "groq"
        elif settings.gemini_api_key:
            _llm = ChatGoogleGenerativeAI(
                model=settings.gemini_model,
                temperature=0,
                api_key=settings.gemini_api_key,
            )
            _llm_provider = "gemini"
        else:
            raise RuntimeError("Configure GEMINI_API_KEY or GROQ_API_KEY to use the assistant")
    return _llm

def fallback_llm():
    global _fallback_llm
    if _llm_provider == "groq" and settings.gemini_api_key:
        if _fallback_llm is None:
            _fallback_llm = ChatGoogleGenerativeAI(
                model=settings.gemini_model,
                temperature=0,
                api_key=settings.gemini_api_key,
            )
        return _fallback_llm
    if _llm_provider == "gemini" and settings.groq_api_key:
        if _fallback_llm is None:
            _fallback_llm = ChatGroq(
                model=settings.groq_model,
                temperature=0,
                api_key=settings.groq_api_key,
            )
        return _fallback_llm
    return None

def is_quota_error(error: Exception) -> bool:
    current = error
    seen = set()
    while current is not None and id(current) not in seen:
        seen.add(id(current))
        code = getattr(current, "code", None)
        status_code = getattr(current, "status_code", None)
        response = getattr(current, "response", None)
        if status_code is None and response is not None:
            status_code = getattr(response, "status_code", None)
        if code == 429 or status_code == 429:
            return True

        message = str(current).lower().replace("-", "_")
        if any(term in message for term in (
            "quota",
            "resource_exhausted",
            "rate limit",
            "rate_limit",
            "too many requests",
            "token limit exceeded",
            "tokens per minute",
            "requests per minute",
        )):
            return True
        current = current.__cause__ or current.__context__
    return False

def invoke_with_fallback(primary, fallback, prompt):
    global _primary_quota_exceeded
    if fallback is None:
        return primary.invoke(prompt)
    if _primary_quota_exceeded:
        return fallback.invoke(prompt)
    try:
        return primary.invoke(prompt)
    except Exception as error:
        if is_quota_error(error):
            _primary_quota_exceeded = True
            logger.warning(
                "Primary %s quota/rate limit reached; routing subsequent model calls to %s",
                _llm_provider,
                "Gemini" if _llm_provider == "groq" else "Groq",
            )
        logger.warning("Primary %s LLM request failed; trying fallback: %s", _llm_provider, error)
        return fallback.invoke(prompt)

def invoke_llm(prompt: str):
    primary = llm()
    fallback = fallback_llm()
    return invoke_with_fallback(primary, fallback, prompt)

def structured_llm(schema, method: str):
    primary = llm().with_structured_output(schema, method=method)
    fallback = fallback_llm()
    fallback_structured = (
        fallback.with_structured_output(schema, method=method)
        if fallback is not None
        else None
    )
    return RunnableLambda(
        lambda prompt: invoke_with_fallback(primary, fallback_structured, prompt)
    )

def web_search_tool():
    global _web_search
    if _web_search is None:
        if not settings.tavily_api_key:
            raise RuntimeError("TAVILY_API_KEY is missing")
        _web_search = TavilySearch(
            tavily_api_key=settings.tavily_api_key,
            max_results=5,
            topic="general",
            include_answer=True,
            include_raw_content=False,
        )
    return _web_search

def add_trace(state: AgentState, message: str):
    return [*state.get("trace", []), message]

def response_text(value) -> str:
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, list):
        parts = []
        for part in value:
            if isinstance(part, str):
                parts.append(part)
            elif isinstance(part, dict) and isinstance(part.get("text"), str):
                parts.append(part["text"])
        return "\n".join(parts).strip()
    return ""

def generated_answer(state: AgentState, response, source: str, trace_message: str):
    answer = response_text(getattr(response, "content", None))
    if not answer:
        logger.error("The %s answer-generation step returned empty content", source)
        return {
            "answer": "I couldn't generate an answer this time. Please try again, or contact the IT help desk if the problem continues.",
            "source_used": "generation_error",
            "trace": add_trace(state, f"{source} answer generation returned empty content"),
        }
    return {
        "answer": answer,
        "source_used": source,
        "trace": add_trace(state, trace_message),
    }

def route_question(state: AgentState):
    router = structured_llm(RouteDecision, method="json_mode")
    decision = router.invoke(f"""
You route messages for an enterprise IT support assistant.
Use kb for questions about company IT policies, VPN, password reset, MFA, laptop setup,
software access, security, email, devices, troubleshooting, or technology support.
Use direct only for greetings, thanks, or casual chat that needs no company knowledge.
Question: {state['question']}
Return valid JSON like {{"route":"kb"}}.
""")
    return {"source_used": decision.route, "trace": add_trace(state, f"Router → {decision.route.upper()}")}

def route_after_router(state: AgentState) -> Literal["retrieve_kb", "direct_answer"]:
    return "retrieve_kb" if state["source_used"] == "kb" else "direct_answer"

def retrieve_kb(state: AgentState):
    logger.info("Starting private knowledge retrieval")
    started_at = time.monotonic()
    retriever = get_retriever()
    logger.info("Initialized private knowledge retriever in %.2f seconds", time.monotonic() - started_at)
    started_at = time.monotonic()
    retrieved_docs = retriever.invoke(state["current_query"])
    logger.info("Completed private knowledge vector search in %.2f seconds", time.monotonic() - started_at)
    docs = []
    seen_chunks = set()
    for document in retrieved_docs:
        identity = (
            document.metadata.get("source", ""),
            document.metadata.get("start_index"),
            document.page_content,
        )
        if identity in seen_chunks:
            continue
        seen_chunks.add(identity)
        docs.append(document)
        if len(docs) == settings.top_k:
            break
    return {"kb_docs": docs, "trace": add_trace(state, f"Private KB retrieval → {len(docs)} chunks")}

def grade_kb(state: AgentState):
    if not state["kb_docs"]:
        return {
            "kb_grade": "weak",
            "trace": add_trace(state, "KB evidence grade → WEAK (no documents retrieved)"),
        }
    grader = structured_llm(EvidenceGrade, method="json_mode")
    context = "\n\n".join(f"Source: {d.metadata.get('source','unknown')}\n{d.page_content}" for d in state["kb_docs"])
    grade = grader.invoke(f"""
You grade evidence for an enterprise IT support assistant.
Question: {state['question']}
Private company KB evidence:\n{context}
Return good only if the evidence is sufficient to answer confidently and specifically.
Otherwise return weak. JSON: {{"grade":"good"}} or {{"grade":"weak"}}.
""")
    return {"kb_grade": grade.grade, "trace": add_trace(state, f"KB evidence grade → {grade.grade.upper()}")}

def after_kb(state: AgentState) -> Literal["generate_from_kb", "search_web"]:
    return "generate_from_kb" if state["kb_grade"] == "good" else "search_web"

def search_web(state: AgentState):
    result = web_search_tool().invoke({"query": state["current_query"]})
    lines, citations = [], []
    if isinstance(result, dict):
        search_answer = response_text(result.get("answer"))
        if search_answer:
            lines.append("Search answer: " + search_answer)
        results = result.get("results", [])
        for item in (results if isinstance(results, list) else []):
            if not isinstance(item, dict):
                continue
            title, url, content = item.get("title", ""), item.get("url", ""), item.get("content", "")
            content = response_text(content)
            if content or title or url:
                lines.append(f"Title: {title}\nURL: {url}\nContent: {content}")
                citations.append({"title": title or url, "url": url, "type": "web"})
    elif isinstance(result, str) and result.strip():
        lines.append(result.strip())
    return {
        "web_results": "\n\n".join(lines),
        "citations": citations,
        "source_used": "web",
        "trace": add_trace(state, "Web fallback → Tavily search"),
    }

def grade_web(state: AgentState):
    if not state["web_results"].strip():
        return {
            "web_grade": "weak",
            "trace": add_trace(state, "Web evidence grade → WEAK (no search results)"),
        }
    grader = structured_llm(EvidenceGrade, method="json_mode")
    grade = grader.invoke(f"""
Question: {state['question']}
Web evidence:\n{state['web_results']}
Return good if the evidence is sufficient and directly relevant; otherwise weak.
Return valid JSON like {{"grade":"good"}}.
""")
    return {"web_grade": grade.grade, "trace": add_trace(state, f"Web evidence grade → {grade.grade.upper()}")}

def after_web(state: AgentState) -> Literal["generate_from_web", "rewrite_query", "insufficient"]:
    if state["web_grade"] == "good":
        return "generate_from_web"
    if state["retry_count"] < settings.max_retries:
        return "rewrite_query"
    return "insufficient"

def rewrite_query(state: AgentState):
    rewritten = response_text(invoke_llm(f"""
Rewrite this IT support question for better private knowledge retrieval and vendor web search.
Preserve intent, add useful technical keywords, do not answer, return only the query.
Question: {state['question']}
""").content)
    if not rewritten:
        rewritten = state["current_query"]
        logger.warning("Query rewriting returned empty content; retrying with the existing query")
    return {
        "current_query": rewritten,
        "retry_count": state["retry_count"] + 1,
        "trace": add_trace(state, f"Query rewrite → {rewritten}"),
    }

def generate_from_kb(state: AgentState):
    context = "\n\n".join(f"[Source: {d.metadata.get('source','unknown')}]\n{d.page_content}" for d in state["kb_docs"])
    response = invoke_llm(f"""
You are an enterprise IT support copilot. Answer ONLY from the private company KB below.
Be concise, actionable, and safe. If steps are present, present them clearly.
Do not invent policy details. Mention that the answer is based on the company's private knowledge base.
Question: {state['question']}\n\nPrivate KB:\n{context}
""")
    citations = []
    seen = set()
    for d in state["kb_docs"]:
        src = d.metadata.get("source", "Private KB")
        if src not in seen:
            seen.add(src)
            citations.append({"title": src.split("/")[-1], "url": "", "type": "private_kb"})
    return {
        **generated_answer(state, response, "private_kb", "Answer generation → PRIVATE KB"),
        "citations": citations,
    }

def generate_from_web(state: AgentState):
    response = invoke_llm(f"""
You are an enterprise IT support copilot. The private company KB was insufficient.
Answer ONLY from the web evidence below. Clearly say this is external web information and may need IT validation before changing company-managed systems.
Question: {state['question']}\n\nWeb evidence:\n{state['web_results']}
""")
    return generated_answer(state, response, "web_search", "Answer generation → WEB SEARCH")

def direct_answer(state: AgentState):
    response = invoke_llm(f"Respond briefly and naturally to: {state['question']}")
    return generated_answer(state, response, "direct", "Direct response → no retrieval")

def insufficient(state: AgentState):
    return {
        "answer": "I couldn't find enough reliable evidence in the company knowledge base or external search to answer confidently. Please contact the IT help desk or provide more details.",
        "source_used": "insufficient_evidence",
        "trace": add_trace(state, "Stopped → insufficient reliable evidence"),
    }

def build_graph():
    graph = StateGraph(AgentState)
    for name, fn in {
        "route_question": route_question,
        "retrieve_kb": retrieve_kb,
        "grade_kb": grade_kb,
        "search_web": search_web,
        "grade_web": grade_web,
        "rewrite_query": rewrite_query,
        "generate_from_kb": generate_from_kb,
        "generate_from_web": generate_from_web,
        "direct_answer": direct_answer,
        "insufficient": insufficient,
    }.items():
        graph.add_node(name, fn)

    graph.add_edge(START, "route_question")
    graph.add_conditional_edges("route_question", route_after_router, {
        "retrieve_kb": "retrieve_kb", "direct_answer": "direct_answer"
    })
    graph.add_edge("retrieve_kb", "grade_kb")
    graph.add_conditional_edges("grade_kb", after_kb, {
        "generate_from_kb": "generate_from_kb", "search_web": "search_web"
    })
    graph.add_edge("search_web", "grade_web")
    graph.add_conditional_edges("grade_web", after_web, {
        "generate_from_web": "generate_from_web", "rewrite_query": "rewrite_query", "insufficient": "insufficient"
    })
    graph.add_edge("rewrite_query", "retrieve_kb")
    graph.add_edge("generate_from_kb", END)
    graph.add_edge("generate_from_web", END)
    graph.add_edge("direct_answer", END)
    graph.add_edge("insufficient", END)
    return graph.compile()

agent_graph = build_graph()

def ask_question(question: str):
    initial: AgentState = {
        "question": question,
        "current_query": question,
        "kb_docs": [],
        "web_results": "",
        "kb_grade": "",
        "web_grade": "",
        "answer": "",
        "source_used": "",
        "retry_count": 0,
        "trace": [],
        "citations": [],
    }
    return agent_graph.invoke(
        initial,
        config={"recursion_limit": max(25, (settings.max_retries + 1) * 6 + 10)},
    )
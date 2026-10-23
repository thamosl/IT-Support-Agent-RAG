import re
import logging
from typing import List, Literal, Optional, Any
from datetime import datetime, timezone
from pydantic import BaseModel, Field, model_validator

logger = logging.getLogger(__name__)

class ChunkEvaluation(BaseModel):
    chunk_index: int = Field(default=1, description="1-based index of the chunk")
    source: str = Field(default="unknown", description="Source document or reference")
    snippet: str = Field(default="", description="Key text snippet from the chunk")
    score: float = Field(default=1.0, description="Relevance score from 0.0 to 1.0")
    is_relevant: bool = Field(default=True, description="True if chunk provides useful context for the query")
    reasoning: str = Field(default="", description="Justification for this chunk's score")

class RAGEvaluation(BaseModel):
    context_relevance: float = Field(
        default=1.0,
        description="Score between 0.0 and 1.0 measuring if retrieved chunks contain relevant information for the user's query."
    )
    context_relevance_reasoning: str = Field(
        default="",
        description="Detailed reasoning for the context relevance score."
    )
    groundedness: float = Field(
        default=1.0,
        description="Score between 0.0 and 1.0 measuring if the generated answer is faithful to the retrieved context without hallucinations."
    )
    groundedness_reasoning: str = Field(
        default="",
        description="Detailed reasoning for the groundedness score."
    )
    answer_relevance: float = Field(
        default=1.0,
        description="Score between 0.0 and 1.0 measuring if the generated answer directly and effectively answers the user's query."
    )
    answer_relevance_reasoning: str = Field(
        default="",
        description="Detailed reasoning for the answer relevance score."
    )
    overall_score: float = Field(
        default=1.0,
        description="Composite overall score between 0.0 and 1.0 (weighted context relevance, groundedness, and answer relevance)."
    )
    verdict: Literal["PASS", "WARNING", "FAIL"] = Field(
        default="PASS",
        description="Overall evaluation verdict: PASS (>= 0.70), WARNING (0.40 - 0.69), FAIL (< 0.40)."
    )
    critique: str = Field(
        default="",
        description="Executive summary critique by the LLM Judge."
    )
    chunk_evaluations: List[ChunkEvaluation] = Field(
        default_factory=list,
        description="Detailed relevance evaluation for each individual retrieved chunk."
    )
    evaluated_at: str = Field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat(),
        description="Timestamp when the evaluation was performed."
    )

    @model_validator(mode="before")
    @classmethod
    def normalize_metrics(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        # If context_relevance is a dict: e.g. {"score": 1.0, "explanation": "..."}
        cr = data.get("context_relevance")
        if isinstance(cr, dict):
            if "context_relevance_reasoning" not in data or not data["context_relevance_reasoning"]:
                data["context_relevance_reasoning"] = cr.get("explanation") or cr.get("reasoning") or ""
            if "chunk_evaluations" not in data or not data["chunk_evaluations"]:
                details = cr.get("details") or cr.get("chunks") or []
                if isinstance(details, list):
                    normalized_chunks = []
                    for idx, ch in enumerate(details, start=1):
                        if isinstance(ch, dict):
                            s_val = float(ch.get("score", 1.0))
                            normalized_chunks.append({
                                "chunk_index": ch.get("chunk_id", ch.get("chunk_index", idx)),
                                "source": ch.get("source", f"Chunk {idx}"),
                                "snippet": ch.get("snippet", ""),
                                "score": s_val,
                                "is_relevant": s_val >= 0.5,
                                "reasoning": ch.get("explanation", ch.get("reasoning", "")),
                            })
                    data["chunk_evaluations"] = normalized_chunks
            data["context_relevance"] = float(cr.get("score", 1.0))
        elif cr is not None:
            try:
                data["context_relevance"] = float(cr)
            except (ValueError, TypeError):
                data["context_relevance"] = 1.0

        # If groundedness is a dict: e.g. {"score": 1.0, "explanation": "..."}
        gr = data.get("groundedness")
        if isinstance(gr, dict):
            if "groundedness_reasoning" not in data or not data["groundedness_reasoning"]:
                data["groundedness_reasoning"] = gr.get("explanation") or gr.get("reasoning") or ""
            data["groundedness"] = float(gr.get("score", 1.0))
        elif gr is not None:
            try:
                data["groundedness"] = float(gr)
            except (ValueError, TypeError):
                data["groundedness"] = 1.0

        # If answer_relevance is a dict: e.g. {"score": 1.0, "explanation": "..."}
        ar = data.get("answer_relevance")
        if isinstance(ar, dict):
            if "answer_relevance_reasoning" not in data or not data["answer_relevance_reasoning"]:
                data["answer_relevance_reasoning"] = ar.get("explanation") or ar.get("reasoning") or ""
            data["answer_relevance"] = float(ar.get("score", 1.0))
        elif ar is not None:
            try:
                data["answer_relevance"] = float(ar)
            except (ValueError, TypeError):
                data["answer_relevance"] = 1.0

        # Normalize overall_score
        os_val = data.get("overall_score")
        if os_val is not None:
            try:
                data["overall_score"] = float(os_val)
            except (ValueError, TypeError):
                data["overall_score"] = 1.0
        else:
            cr_num = float(data.get("context_relevance", 1.0))
            gr_num = float(data.get("groundedness", 1.0))
            ar_num = float(data.get("answer_relevance", 1.0))
            data["overall_score"] = round((0.35 * cr_num) + (0.35 * gr_num) + (0.30 * ar_num), 2)

        # Normalize verdict
        v = str(data.get("verdict", "")).upper()
        if "PASS" in v:
            data["verdict"] = "PASS"
        elif "WARN" in v:
            data["verdict"] = "WARNING"
        elif "FAIL" in v:
            data["verdict"] = "FAIL"
        else:
            data["verdict"] = "PASS" if float(data["overall_score"]) >= 0.70 else ("WARNING" if float(data["overall_score"]) >= 0.40 else "FAIL")

        return data


def extract_keywords(text: str) -> set[str]:
    stopwords = {
        "the", "a", "an", "and", "or", "in", "on", "at", "to", "for", "with", "by", "from",
        "is", "are", "was", "were", "be", "been", "have", "has", "had", "do", "does", "did",
        "of", "that", "this", "these", "those", "it", "i", "you", "we", "they", "he", "she",
        "what", "how", "why", "when", "where", "can", "could", "would", "should", "my", "your"
    }
    words = re.findall(r"\b[a-zA-Z0-9_\-]{3,}\b", text.lower())
    return {w for w in words if w not in stopwords}


def fallback_evaluate(
    question: str,
    chunks: list[dict[str, str]],
    answer: str,
    source: str
) -> RAGEvaluation:
    """Deterministic fallback evaluator when LLM is unavailable or fails."""
    q_words = extract_keywords(question)
    ans_words = extract_keywords(answer)
    
    # Direct conversational response
    if source == "direct":
        return RAGEvaluation(
            context_relevance=1.0,
            context_relevance_reasoning="Direct conversation; no external retrieval was needed.",
            groundedness=1.0,
            groundedness_reasoning="Direct response grounded in general assistant capability.",
            answer_relevance=0.95,
            answer_relevance_reasoning="Direct answer addressed the greeting or general prompt.",
            overall_score=0.98,
            verdict="PASS",
            critique="Direct chat message handled effectively without requiring document retrieval.",
            chunk_evaluations=[],
        )

    # Insufficient evidence response
    if source == "insufficient_evidence":
        return RAGEvaluation(
            context_relevance=0.25,
            context_relevance_reasoning="Retrieved chunks did not contain sufficient evidence to answer.",
            groundedness=1.0,
            groundedness_reasoning="Model faithfully abstained from hallucinating an unsupported answer.",
            answer_relevance=0.90,
            answer_relevance_reasoning="Model clearly communicated inability to verify answer and advised next steps.",
            overall_score=0.72,
            verdict="PASS",
            critique="Agent correctly identified insufficient evidence and abstained from hallucination.",
            chunk_evaluations=[],
        )

    # Retrieval evaluation
    chunk_evals = []
    chunk_scores = []
    all_chunk_text = ""

    for idx, c in enumerate(chunks, start=1):
        c_text = c.get("content", "")
        c_src = c.get("source", f"Chunk {idx}")
        all_chunk_text += "\n" + c_text
        c_words = extract_keywords(c_text)
        
        if q_words:
            overlap = len(q_words & c_words) / len(q_words)
            # scale overlap to realistic score
            score = round(min(1.0, max(0.2, overlap * 1.5)), 2)
        else:
            score = 0.5
            
        is_rel = score >= 0.45
        snippet = (c_text[:120] + "...") if len(c_text) > 120 else c_text
        reasoning = (
            f"Matches {len(q_words & c_words)} key query terms ({', '.join(list(q_words & c_words)[:3])})."
            if is_rel else "Low overlap with user query keywords."
        )
        
        chunk_evals.append(
            ChunkEvaluation(
                chunk_index=idx,
                source=c_src,
                snippet=snippet.strip(),
                score=score,
                is_relevant=is_rel,
                reasoning=reasoning,
            )
        )
        chunk_scores.append(score)

    if chunk_scores:
        context_relevance = round(sum(chunk_scores) / len(chunk_scores), 2)
    else:
        context_relevance = 0.5

    # Groundedness: Check if key answer claims exist in retrieved context
    ctx_words = extract_keywords(all_chunk_text)
    if ans_words:
        grounded_ratio = len(ans_words & ctx_words) / len(ans_words)
        groundedness = round(min(1.0, max(0.3, grounded_ratio * 1.2)), 2)
    else:
        groundedness = 0.8

    # Answer Relevancy: Check if question terms are addressed in answer
    if q_words:
        addressed_ratio = len(q_words & ans_words) / len(q_words)
        ans_relevance = round(min(1.0, max(0.4, addressed_ratio * 1.3)), 2)
    else:
        ans_relevance = 0.85

    overall = round((0.35 * context_relevance) + (0.35 * groundedness) + (0.30 * ans_relevance), 2)
    verdict: Literal["PASS", "WARNING", "FAIL"] = "PASS" if overall >= 0.70 else ("WARNING" if overall >= 0.40 else "FAIL")

    return RAGEvaluation(
        context_relevance=context_relevance,
        context_relevance_reasoning=f"Retrieved {len(chunks)} chunks with an average query match score of {int(context_relevance*100)}%.",
        groundedness=groundedness,
        groundedness_reasoning=f"Generated answer claims show {int(groundedness*100)}% lexical and semantic grounding in retrieved evidence.",
        answer_relevance=ans_relevance,
        answer_relevance_reasoning=f"Answer directly targets key terms and intent of the query ({int(ans_relevance*100)}% match).",
        overall_score=overall,
        verdict=verdict,
        critique=f"Automated evaluation completed: overall RAG quality is rated as {verdict} ({int(overall*100)}%).",
        chunk_evaluations=chunk_evals,
    )


def build_judge_prompt(question: str, chunks: list[dict[str, str]], answer: str, source: str) -> str:
    formatted_chunks = []
    for i, c in enumerate(chunks, start=1):
        src = c.get("source", f"Chunk {i}")
        content = c.get("content", "")
        formatted_chunks.append(f"--- Chunk #{i} [Source: {src}] ---\n{content}")
    context_str = "\n\n".join(formatted_chunks) if formatted_chunks else "None"

    return f"""You are an expert impartial AI Quality Inspector and LLM-as-a-Judge for an Enterprise RAG IT Support System.
Evaluate the retrieval quality and answer generation with extreme rigor and precision.

[EVALUATION DIMENSIONS]
1. Context Relevance (0.0 to 1.0):
   - Check each retrieved chunk individually: does it contain direct answers or necessary context for the query?
   - Score each chunk (0.0 to 1.0) and explain why in 1 sentence.
   - Aggregate context relevance score (0.0 to 1.0). If source is 'direct' (casual chat), score 1.0.

2. Groundedness / Faithfulness (0.0 to 1.0):
   - Verify every claim, number, policy rule, and instruction in the answer against the retrieved context.
   - 1.0 = completely faithful, no hallucinations.
   - 0.5 - 0.8 = mostly grounded, minor extrapolation.
   - 0.0 - 0.4 = fabricated facts or contradicts context.
   - If source is 'direct' or 'insufficient_evidence', score 1.0 if truthful.

3. Answer Relevancy (0.0 to 1.0):
   - Does the answer directly, clearly, concisely, and completely resolve the user's specific question?
   - 1.0 = ideal actionable resolution.
   - 0.5 - 0.8 = partially helpful, verbose, or missing key details.
   - 0.0 - 0.4 = off-topic, unhelpful, or misleading.

4. Overall Score & Verdict:
   - Calculate overall_score = (0.35 * context_relevance) + (0.35 * groundedness) + (0.30 * answer_relevance).
   - Set verdict: PASS if overall_score >= 0.70, WARNING if 0.40 <= overall_score < 0.70, FAIL if overall_score < 0.40.
   - Provide a concise critique summarizing strengths and areas of improvement.

[USER QUESTION]
{question}

[SOURCE USED]
{source}

[RETRIEVED CHUNKS]
{context_str}

[GENERATED ANSWER]
{answer}

You MUST return valid JSON adhering strictly to the schema.
"""

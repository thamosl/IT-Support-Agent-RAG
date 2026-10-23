import json
import sqlite3
from datetime import datetime, timezone
from typing import Any
from app.core.config import get_settings

settings = get_settings()
_db_initialized = False

def init_db() -> None:
    global _db_initialized
    con = sqlite3.connect(settings.audit_db_path)
    con.execute(
        """CREATE TABLE IF NOT EXISTS query_audit (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           created_at TEXT NOT NULL,
           question TEXT NOT NULL, 
           source_used TEXT NOT NULL,
           trace_json TEXT NOT NULL,
           evaluation_json TEXT
        )"""
    )
    # Ensure backward compatibility if table existed without evaluation_json
    cur = con.cursor()
    cur.execute("PRAGMA table_info(query_audit)")
    columns = [col[1] for col in cur.fetchall()]
    if "evaluation_json" not in columns:
        con.execute("ALTER TABLE query_audit ADD COLUMN evaluation_json TEXT")
    con.commit()
    con.close()
    _db_initialized = True

def _ensure_db() -> None:
    global _db_initialized
    if not _db_initialized:
        init_db()

def write_audit(
    question: str,
    source_used: str,
    trace: list[str],
    evaluation: dict[str, Any] | None = None
) -> None:
    _ensure_db()
    con = sqlite3.connect(settings.audit_db_path)
    eval_text = json.dumps(evaluation) if evaluation else "{}"
    con.execute(
        "INSERT INTO query_audit(created_at, question, source_used, trace_json, evaluation_json) VALUES (?,?,?,?,?)",
        (datetime.now(timezone.utc).isoformat(), question, source_used, json.dumps(trace), eval_text)
    )
    con.commit()
    con.close()

def get_recent_audits(limit: int = 50) -> list[dict[str, Any]]:
    _ensure_db()
    con = sqlite3.connect(settings.audit_db_path)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute(
        "SELECT id, created_at, question, source_used, trace_json, evaluation_json FROM query_audit ORDER BY id DESC LIMIT ?",
        (limit,)
    )
    rows = cur.fetchall()
    con.close()

    results = []
    for row in rows:
        trace = []
        evaluation = {}
        try:
            trace = json.loads(row["trace_json"]) if row["trace_json"] else []
        except Exception:
            trace = []
        try:
            evaluation = json.loads(row["evaluation_json"]) if row["evaluation_json"] else {}
        except Exception:
            evaluation = {}

        results.append({
            "id": row["id"],
            "created_at": row["created_at"],
            "question": row["question"],
            "source_used": row["source_used"],
            "trace": trace,
            "evaluation": evaluation
        })
    return results

def get_evaluations_summary() -> dict[str, Any]:
    _ensure_db()
    con = sqlite3.connect(settings.audit_db_path)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT evaluation_json FROM query_audit WHERE evaluation_json IS NOT NULL AND evaluation_json != '' AND evaluation_json != '{}'")
    rows = cur.fetchall()
    con.close()

    total = 0
    passes = 0
    total_score = 0.0
    total_context_rel = 0.0
    total_groundedness = 0.0
    total_answer_rel = 0.0

    for row in rows:
        try:
            data = json.loads(row["evaluation_json"])
            if not data or not isinstance(data, dict):
                continue
            total += 1
            score = float(data.get("overall_score", 0.0))
            total_score += score
            total_context_rel += float(data.get("context_relevance", 0.0))
            total_groundedness += float(data.get("groundedness", 0.0))
            total_answer_rel += float(data.get("answer_relevance", 0.0))
            if data.get("verdict") == "PASS":
                passes += 1
        except Exception:
            continue

    if total == 0:
        return {
            "total_evaluated": 0,
            "pass_rate": 100.0,
            "avg_overall_score": 0.0,
            "avg_context_relevance": 0.0,
            "avg_groundedness": 0.0,
            "avg_answer_relevance": 0.0,
        }

    return {
        "total_evaluated": total,
        "pass_rate": round((passes / total) * 100, 1),
        "avg_overall_score": round(total_score / total, 2),
        "avg_context_relevance": round(total_context_rel / total, 2),
        "avg_groundedness": round(total_groundedness / total, 2),
        "avg_answer_relevance": round(total_answer_rel / total, 2),
    }
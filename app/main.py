import os
import logging
from pathlib import Path

from app.core.logging import configure_logging
from app.core.config import get_settings, BASE_DIR

configure_logging()
logger = logging.getLogger(__name__)
settings = get_settings()

# ── LangSmith tracing setup ─────────────────────────────────────────
def configure_langsmith() -> None:
    """Synchronize LangSmith / LangChain env vars before initializing any pipelines.
    Crucially strips out any conflicting LANGSMITH_AGENT_* variables that cause
    the LangSmith tracer to suppress/drop traces.
    """
    # Remove agent addressing variables that trigger LangSmith routing conflict
    for bad_key in ("LANGSMITH_AGENT_ID", "LANGSMITH_AGENT_ENVIRONMENT"):
        os.environ.pop(bad_key, None)

    api_key = (
        getattr(settings, "langsmith_api_key", "")
        or getattr(settings, "langchain_api_key", "")
        or os.environ.get("LANGSMITH_API_KEY", "")
        or os.environ.get("LANGCHAIN_API_KEY", "")
    )
    project = (
        getattr(settings, "langsmith_project", "")
        or os.environ.get("LANGSMITH_PROJECT", "")
        or os.environ.get("LANGCHAIN_PROJECT", "")
        or "IT SUPPORT Agentic rag"
    )
    endpoint = (
        getattr(settings, "langsmith_endpoint", "")
        or os.environ.get("LANGSMITH_ENDPOINT", "")
        or os.environ.get("LANGCHAIN_ENDPOINT", "")
        or "https://api.smith.langchain.com"
    )
    tracing_flag = (
        str(getattr(settings, "langsmith_tracing", "true")).lower() in ("true", "1")
        or os.environ.get("LANGSMITH_TRACING", "").lower() in ("true", "1")
        or os.environ.get("LANGCHAIN_TRACING_V2", "").lower() in ("true", "1")
    )

    if api_key:
        os.environ["LANGSMITH_API_KEY"] = api_key
        os.environ["LANGCHAIN_API_KEY"] = api_key
    if project:
        os.environ["LANGSMITH_PROJECT"] = project
        os.environ["LANGCHAIN_PROJECT"] = project
    if endpoint:
        os.environ["LANGSMITH_ENDPOINT"] = endpoint
        os.environ["LANGCHAIN_ENDPOINT"] = endpoint

    if tracing_flag and api_key:
        os.environ["LANGSMITH_TRACING"] = "true"
        os.environ["LANGCHAIN_TRACING_V2"] = "true"
        logger.info(
            "LangSmith tracing ENABLED  → project=%s  endpoint=%s",
            project,
            endpoint,
        )
    else:
        reason = "no API key configured" if not api_key else "tracing=false"
        logger.info("LangSmith tracing DISABLED (%s)", reason)

    # Clear cached env var values if langsmith was loaded earlier
    try:
        from langsmith import utils as ls_utils
        if hasattr(ls_utils.get_env_var, "cache_clear"):
            ls_utils.get_env_var.cache_clear()
    except Exception:
        pass

# Must be called BEFORE importing workflow or routes so LangChain tracers initialize correctly
configure_langsmith()

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.api.routes import router
from app.services.audit import init_db

init_db()

app = FastAPI(title=settings.app_name, version="1.0.0")

app.include_router(router)
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(name="index.html", request=request, context={"app_name": settings.app_name})
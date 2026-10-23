from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.api.routes import router
from app.core.config import get_settings, BASE_DIR
from app.core.logging import configure_logging
from app.services.audit import init_db

import os
import logging

configure_logging()
logger = logging.getLogger(__name__)
settings= get_settings()

# ── LangSmith tracing setup ─────────────────────────────────────────
def configure_langsmith() -> None:
    """Push LangSmith env vars from pydantic Settings into os.environ
    so the langsmith / langchain SDKs pick them up automatically."""
    mapping = {
        "LANGSMITH_API_KEY": settings.langsmith_api_key,
        "LANGSMITH_PROJECT": settings.langsmith_project,
        "LANGSMITH_ENDPOINT": settings.langsmith_endpoint,
        "LANGSMITH_TRACING": settings.langsmith_tracing,
    }
    for key, value in mapping.items():
        if value:
            os.environ.setdefault(key, value)

    tracing_enabled = os.environ.get("LANGSMITH_TRACING", "false").lower() == "true"
    if tracing_enabled and settings.langsmith_api_key:
        logger.info(
            "LangSmith tracing ENABLED  → project=%s  endpoint=%s",
            os.environ.get("LANGSMITH_PROJECT"),
            os.environ.get("LANGSMITH_ENDPOINT"),
        )
    else:
        reason = "no API key" if not settings.langsmith_api_key else "tracing=false"
        logger.info("LangSmith tracing DISABLED (%s)", reason)

configure_langsmith()
init_db()

app= FastAPI(title=settings.app_name, version= "1.0.0")

app.include_router(router)
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name= "static")
templates= Jinja2Templates(directory=str(BASE_DIR / "templates"))

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(name= "index.html", request=  request, context= {"app_name": settings.app_name})
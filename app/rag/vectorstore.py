import logging
import time
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from app.core.config import BASE_DIR, get_settings

settings= get_settings()
logger = logging.getLogger(__name__)

_embeddings= None
_vectorstore= None

EMBEDDING_DIMENTIONS= {
    "gemini-embedding-2-preview-small" : 768,
    "gemini-embedding-2-preview-medium" : 1536,
    "gemini-embedding-2-preview" : 3072,
    "sentence-transformers/all-minilm-l6-v2": 384
}

def get_embedding_dimention(model_name: str | None = None) -> int:
    name= (model_name or settings.embedding_model or "").strip()
    if not name:
        raise RuntimeError("Embedding Model is Not Configured")

    normalized= name.lower()
    if normalized in EMBEDDING_DIMENTIONS:
        return EMBEDDING_DIMENTIONS[normalized]
    if "gemini-embedding-2-preview-small" in normalized:
        return 768
    if "gemini-embedding-2-preview-medium" in normalized:
        return 1536
    if "gemini-embedding-2-preview-large" in normalized:
        return 3072
    raise ValueError(
        f"Unsupported Embedding Model '{model_name or settings.embedding_model}' for pinecone."
        "Add the matching dimention to EMBDDING_DIMENTIONS."
    )

def get_embeddings():
    global _embeddings

    if _embeddings is None:
        model_name = settings.embedding_model.strip()
        if model_name.lower().startswith("sentence-transformers/"):
            started_at = time.monotonic()
            logger.info("Initializing FastEmbed model '%s'", model_name)
            _embeddings = FastEmbedEmbeddings(
                model_name=model_name,
                cache_dir=str(BASE_DIR / ".cache" / "fastembed"),
                threads=1,
            )
            logger.info(
                "Initialized FastEmbed model '%s' in %.2f seconds",
                model_name,
                time.monotonic() - started_at,
            )
        else:
            if not settings.gemini_api_key:
                raise RuntimeError("GEMINI_API_KEY Missing")
            _embeddings = GoogleGenerativeAIEmbeddings(
                model=model_name,
                api_key=settings.gemini_api_key
            )
    return  _embeddings

def ensure_index():
    if not settings.pinecone_api_key:
        raise RuntimeError("Pinecone API is Missing")

    desired_dimention= get_embedding_dimention()
    pc= Pinecone(api_key= settings.pinecone_api_key)
    logger.info("Checking Pinecone index '%s'", settings.pinecone_index_name)
    started_at = time.monotonic()
    names= [x["name"] for x in pc.list_indexes()]
    logger.info("Listed Pinecone indexes in %.2f seconds", time.monotonic() - started_at)

    if settings.pinecone_index_name in names:
        started_at = time.monotonic()
        index_info= pc.describe_index(settings.pinecone_index_name)
        logger.info(
            "Described Pinecone index '%s' in %.2f seconds",
            settings.pinecone_index_name,
            time.monotonic() - started_at,
        )
        current_dimention= getattr(index_info, "dimension", None)
        if current_dimention is None and isinstance(index_info, dict):
            current_dimention= index_info.get("dimension")

        if current_dimention != desired_dimention:
            raise ValueError(
                f"Pinecone index '{settings.pinecone_index_name}' has dimension "
                f"{current_dimention}, but embedding model '{settings.embedding_model}' "
                f"requires dimension {desired_dimention}. Use an index with the matching "
                "dimension or recreate this index intentionally."
            )

    else:
        pc.create_index(
            name= settings.pinecone_index_name,
            dimension= desired_dimention,
            metric= "cosine",
            spec= ServerlessSpec(cloud= "aws", region= "us-east-1")
        )

        while not pc.describe_index(settings.pinecone_index_name).status["ready"]:
            time.sleep(1)

    return pc.Index(settings.pinecone_index_name)


def get_vectorstore():
    global _vectorstore
    if _vectorstore is None:
        index= ensure_index()
        _vectorstore= PineconeVectorStore(
            index= index,
            embedding= get_embeddings(),
            namespace= settings.pinecone_namespace
        )
    return _vectorstore

def get_retriever():
    fetch_k = max(settings.top_k * 4, settings.top_k)
    return get_vectorstore().as_retriever(search_kwargs={"k": fetch_k})

def add_documents(chunks):
    store= get_vectorstore()
    return store.add_documents(chunks)
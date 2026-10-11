from pathlib import Path
from app.core.config import get_settings
from app.services.ingestion import load_file, chunk_documents, SUPPORTED
from app.rag.vectorstore import add_documents


def main() -> None:
    settings = get_settings()
    folder = Path(settings.sample_kb_dir)
    if not folder.is_dir():
        raise FileNotFoundError(f"Knowledge-base folder does not exist: {folder}")

    files = sorted(
        path
        for path in folder.iterdir()
        if path.is_file() and path.suffix.lower() in SUPPORTED
    )
    if not files:
        raise FileNotFoundError(f"No supported knowledge-base files found in {folder}")

    all_docs = []
    for path in files:
        all_docs.extend(load_file(path))

    chunks = chunk_documents(all_docs)
    if not chunks:
        raise ValueError(f"No text could be extracted from supported files in {folder}")

    ids = add_documents(chunks)
    print(f"Indexed {len(files)} files -> {len(chunks)} chunks -> {len(ids)} Pinecone vectors")


if __name__ == "__main__":
    main()
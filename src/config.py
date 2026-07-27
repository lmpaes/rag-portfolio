import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
VOYAGE_API_KEY = os.environ.get("VOYAGE_API_KEY", "")

if not ANTHROPIC_API_KEY:
    raise RuntimeError("ANTHROPIC_API_KEY não configurada no .env")
if not VOYAGE_API_KEY:
    raise RuntimeError("VOYAGE_API_KEY não configurada no .env")

LLM_MODEL = "claude-haiku-4-5"
EMBEDDING_MODEL = "voyage-3.5"

BASE_DIR = Path(__file__).resolve().parent.parent
DOCUMENTOS_DIR = BASE_DIR / "documentos"
CHROMA_PERSIST_DIR = BASE_DIR / ".chroma"
CHROMA_COLLECTION_NAME = "base_conhecimento"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
TOP_K = 5

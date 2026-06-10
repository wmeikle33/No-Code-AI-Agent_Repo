from pathlib import Path
import os

ROOT_DIR = Path(__file__).resolve().parent.parent

AGENTS_DIR = ROOT_DIR / "agents"
WORKFLOWS_DIR = ROOT_DIR / "workflows"
DOCS_DIR = ROOT_DIR / "docs"

DEFAULT_MODEL = os.getenv(
    "DEFAULT_MODEL",
    "gpt-4o"
)

LOG_LEVEL = os.getenv(
    "LOG_LEVEL",
    "INFO"
)

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///agents.db"

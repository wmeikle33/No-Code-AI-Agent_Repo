from pathlib import Path
from typing import List


def ensure_directory(path: str) -> Path:
    directory = Path(path)
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def read_text_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def write_text_file(path: str, content: str) -> None:
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)


def list_files(directory: str, suffix: str = "") -> List[str]:
    path = Path(directory)

    if suffix:
        return [str(file) for file in path.rglob(f"*{suffix}")]

    return [str(file) for file in path.rglob("*") if file.is_file()]

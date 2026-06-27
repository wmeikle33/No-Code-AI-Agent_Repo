
import json
from pathlib import Path
from typing import Any


def load_json(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_json(data: dict, path: str) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def pretty_json(data: Any) -> str:
    return json.dumps(data, indent=4, ensure_ascii=False)

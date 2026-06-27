from dataclasses import asdict, is_dataclass
from typing import Any


def to_dict(obj: Any) -> dict:
    if is_dataclass(obj):
        return asdict(obj)

    if hasattr(obj, "__dict__"):
        return vars(obj)

    raise TypeError(
        f"Cannot serialize object of type {type(obj)}"
    )


def serialize_result(
    workflow_name: str,
    result: Any
) -> dict:
    return {
        "workflow": workflow_name,
        "result": result,
    }

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class SchemaValidationResult:
    is_valid: bool
    missing_fields: List[str]
    unexpected_fields: List[str]
    errors: List[str]


def get_required_fields(schema: Dict[str, Any]) -> List[str]:
    """
    Return required fields from a JSON-style schema.
    """
    return schema.get("required", [])


def get_schema_properties(schema: Dict[str, Any]) -> Dict[str, Any]:
    """
    Return schema properties.
    """
    return schema.get("properties", {})


def validate_record_against_schema(
    record: Dict[str, Any],
    schema: Dict[str, Any],
) -> SchemaValidationResult:
    """
    Validate a simple dictionary record against a JSON-style schema.

    This is intentionally lightweight. For full JSON Schema validation,
    use the jsonschema package elsewhere.
    """
    required_fields = get_required_fields(schema)
    properties = get_schema_properties(schema)

    missing_fields = [
        field for field in required_fields
        if field not in record or record[field] in [None, ""]
    ]

    unexpected_fields = [
        field for field in record
        if field not in properties
    ]

    errors = []

    if missing_fields:
        errors.append(
            f"Missing required fields: {', '.join(missing_fields)}"
        )

    if unexpected_fields:
        errors.append(
            f"Unexpected fields: {', '.join(unexpected_fields)}"
        )

    return SchemaValidationResult(
        is_valid=not errors,
        missing_fields=missing_fields,
        unexpected_fields=unexpected_fields,
        errors=errors,
    )


def summarize_schema(schema: Dict[str, Any]) -> Dict[str, Any]:
    """
    Create a compact summary of a schema for agents, routing, or docs.
    """
    properties = get_schema_properties(schema)

    return {
        "title": schema.get("title"),
        "description": schema.get("description"),
        "required_fields": get_required_fields(schema),
        "field_count": len(properties),
        "fields": list(properties.keys()),
    }


def describe_schema_fields(schema: Dict[str, Any]) -> List[Dict[str, Optional[str]]]:
    """
    Return field-level descriptions from a schema.
    """
    properties = get_schema_properties(schema)

    return [
        {
            "name": field_name,
            "type": field_info.get("type"),
            "description": field_info.get("description"),
        }
        for field_name, field_info in properties.items()
    ]


def compare_schema_fields(
    old_schema: Dict[str, Any],
    new_schema: Dict[str, Any],
) -> Dict[str, List[str]]:
    """
    Compare fields between two schema versions.
    """
    old_fields = set(get_schema_properties(old_schema).keys())
    new_fields = set(get_schema_properties(new_schema).keys())

    return {
        "added_fields": sorted(new_fields - old_fields),
        "removed_fields": sorted(old_fields - new_fields),
        "shared_fields": sorted(old_fields & new_fields),
    }


def generate_schema_prompt_context(schema: Dict[str, Any]) -> str:
    """
    Generate a readable schema description for use inside agent prompts.
    """
    summary = summarize_schema(schema)
    fields = describe_schema_fields(schema)

    field_lines = []

    for field in fields:
        line = f"- {field['name']}"

        if field.get("type"):
            line += f" ({field['type']})"

        if field.get("description"):
            line += f": {field['description']}"

        field_lines.append(line)

    required = ", ".join(summary["required_fields"]) or "None"

    return (
        f"Schema: {summary.get('title') or 'Untitled schema'}\n"
        f"Description: {summary.get('description') or 'No description provided.'}\n"
        f"Required fields: {required}\n"
        f"Fields:\n"
        + "\n".join(field_lines)
    )


def check_schema_compatibility(
    source_schema: Dict[str, Any],
    target_schema: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Check whether one schema can reasonably map into another.
    """
    source_fields = set(get_schema_properties(source_schema).keys())
    target_required = set(get_required_fields(target_schema))

    missing_target_required = sorted(target_required - source_fields)

    return {
        "compatible": len(missing_target_required) == 0,
        "missing_target_required_fields": missing_target_required,
    }

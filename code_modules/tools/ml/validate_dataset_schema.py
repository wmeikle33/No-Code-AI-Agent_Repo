def validate_dataset_schema(
    dataset: List[Dict[str, Any]],
    required_fields: List[str],
) -> Dict[str, Any]:
    """Validate that each dataset row contains required fields."""
    missing = []

    for index, row in enumerate(dataset):
        missing_fields = [field for field in required_fields if field not in row]
        if missing_fields:
            missing.append({
                "row_index": index,
                "missing_fields": missing_fields,
            })

    return {
        "valid": len(missing) == 0,
        "missing_field_errors": missing,
        "rows_checked": len(dataset),
    }

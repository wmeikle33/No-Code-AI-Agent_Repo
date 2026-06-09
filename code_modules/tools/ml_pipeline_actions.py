from typing import Any, Dict, List, Optional
import statistics


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


def profile_dataset(dataset: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Generate basic dataset profile statistics."""
    if not dataset:
        return {"row_count": 0, "columns": []}

    columns = list(dataset[0].keys())

    return {
        "row_count": len(dataset),
        "columns": columns,
        "column_count": len(columns),
        "sample_row": dataset[0],
    }


def detect_missing_values(dataset: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Detect missing, empty, or null values by column."""
    missing_counts: Dict[str, int] = {}

    for row in dataset:
        for key, value in row.items():
            if value is None or value == "":
                missing_counts[key] = missing_counts.get(key, 0) + 1

    return {
        "missing_values": missing_counts,
        "has_missing_values": bool(missing_counts),
    }


def split_train_test(
    dataset: List[Dict[str, Any]],
    test_ratio: float = 0.2,
) -> Dict[str, List[Dict[str, Any]]]:
    """Split dataset into train and test sets."""
    if not 0 < test_ratio < 1:
        raise ValueError("test_ratio must be between 0 and 1")

    split_index = int(len(dataset) * (1 - test_ratio))

    return {
        "train": dataset[:split_index],
        "test": dataset[split_index:],
    }


def calculate_class_distribution(
    dataset: List[Dict[str, Any]],
    target_column: str,
) -> Dict[str, Any]:
    """Calculate class distribution for classification tasks."""
    distribution: Dict[str, int] = {}

    for row in dataset:
        label = str(row.get(target_column, "UNKNOWN"))
        distribution[label] = distribution.get(label, 0) + 1

    return {
        "target_column": target_column,
        "distribution": distribution,
        "total_rows": len(dataset),
    }


def generate_feature_summary(
    dataset: List[Dict[str, Any]],
    numeric_columns: List[str],
) -> Dict[str, Any]:
    """Generate simple statistics for numeric features."""
    summary = {}

    for column in numeric_columns:
        values = [
            row[column]
            for row in dataset
            if isinstance(row.get(column), (int, float))
        ]

        if values:
            summary[column] = {
                "min": min(values),
                "max": max(values),
                "mean": statistics.mean(values),
                "median": statistics.median(values),
            }

    return summary


def evaluate_binary_classifier(
    predictions: List[int],
    actuals: List[int],
) -> Dict[str, float]:
    """Evaluate binary classification predictions."""
    if len(predictions) != len(actuals):
        raise ValueError("predictions and actuals must have same length")

    tp = sum(1 for p, a in zip(predictions, actuals) if p == 1 and a == 1)
    tn = sum(1 for p, a in zip(predictions, actuals) if p == 0 and a == 0)
    fp = sum(1 for p, a in zip(predictions, actuals) if p == 1 and a == 0)
    fn = sum(1 for p, a in zip(predictions, actuals) if p == 0 and a == 1)

    accuracy = (tp + tn) / len(actuals) if actuals else 0
    precision = tp / (tp + fp) if tp + fp else 0
    recall = tp / (tp + fn) if tp + fn else 0
    f1 = (
        2 * precision * recall / (precision + recall)
        if precision + recall
        else 0
    )

    return {
        "accuracy": round(accuracy, 4),
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1_score": round(f1, 4),
    }


def generate_model_card(
    model_name: str,
    task_type: str,
    metrics: Dict[str, Any],
    training_data_description: str,
    limitations: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Generate a lightweight model card for documentation."""
    return {
        "model_name": model_name,
        "task_type": task_type,
        "metrics": metrics,
        "training_data": training_data_description,
        "limitations": limitations or [],
        "recommended_use": "Use only for the documented task and data domain.",
    }


def check_model_deployment_readiness(
    metrics: Dict[str, float],
    minimum_accuracy: float = 0.8,
    minimum_f1: float = 0.75,
) -> Dict[str, Any]:
    """Check whether a model meets basic deployment thresholds."""
    accuracy = metrics.get("accuracy", 0)
    f1 = metrics.get("f1_score", 0)

    ready = accuracy >= minimum_accuracy and f1 >= minimum_f1

    return {
        "deployment_ready": ready,
        "accuracy_passed": accuracy >= minimum_accuracy,
        "f1_passed": f1 >= minimum_f1,
        "recommendation": (
            "Ready for staging deployment."
            if ready
            else "Needs additional validation before deployment."
        ),
    }

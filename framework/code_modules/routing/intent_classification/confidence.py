def is_high_confidence(confidence: float, threshold: float = 0.75) -> bool:
    return confidence >= threshold


def requires_clarification(confidence: float, threshold: float = 0.55) -> bool:
    return confidence < threshold


def confidence_band(confidence: float) -> str:
    if confidence >= 0.85:
        return "high"
    if confidence >= 0.65:
        return "medium"
    return "low"

def upgrade_priority(
    current_priority,
    requires_human_review,
    confidence
):
    if requires_human_review:
        return "high"

    if confidence < 0.5:
        return "high"

    return current_priority

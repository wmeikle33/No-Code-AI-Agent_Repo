from .priority_rules import PRIORITY_RULES


def determine_priority(text: str):
    text = text.lower()

    for rule in PRIORITY_RULES:
        for keyword in rule.keywords:
            if keyword in text:
                return {
                    "priority": rule.priority,
                    "reason": rule.reason,
                    "matched_keyword": keyword
                }

    return {
        "priority": "low",
        "reason": "No high-priority indicators found."
    }
}

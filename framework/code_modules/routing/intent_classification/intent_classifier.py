from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .intent_rules import INTENT_RULES


@dataclass
class IntentClassification:
    intent: str
    confidence: float
    matched_terms: List[str] = field(default_factory=list)
    alternatives: Dict[str, float] = field(default_factory=dict)
    explanation: Optional[str] = None


def normalize_text(text: str) -> str:
    return text.lower().strip()


def classify_intent(text: str) -> IntentClassification:
    normalized = normalize_text(text)

    scores = {}
    matches = {}

    for intent, keywords in INTENT_RULES.items():
        matched = [
            keyword for keyword in keywords
            if keyword.lower() in normalized
        ]

        if matched:
            scores[intent] = len(matched) / max(len(keywords), 1)
            matches[intent] = matched

    if not scores:
        return IntentClassification(
            intent="general_assistance",
            confidence=0.35,
            explanation="No clear intent rule matched.",
        )

    sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    best_intent, best_score = sorted_scores[0]

    confidence = min(0.95, 0.45 + best_score)

    return IntentClassification(
        intent=best_intent,
        confidence=round(confidence, 2),
        matched_terms=matches.get(best_intent, []),
        alternatives=dict(sorted_scores[1:4]),
        explanation=f"Matched terms suggest intent: {best_intent}.",
    )


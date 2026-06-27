
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass(frozen=True)
class EscalationRule:
    name: str
    queue: str
    triggers: List[str]
    priority: int
    explanation: str


@dataclass
class EscalationDecision:
    should_escalate: bool
    queue: Optional[str]
    priority: int
    matched_rules: List[str] = field(default_factory=list)
    reasons: List[str] = field(default_factory=list)


ESCALATION_RULES: List[EscalationRule] = [
    EscalationRule(
        name="legal_or_compliance",
        queue="legal_review",
        triggers=[
            "legal",
            "lawsuit",
            "compliance",
            "contract",
            "gdpr",
            "hipaa",
            "data privacy",
        ],
        priority=100,
        explanation="Legal, compliance, or data privacy issue detected.",
    ),
    EscalationRule(
        name="security_incident",
        queue="security_review",
        triggers=[
            "security breach",
            "hacked",
            "unauthorized access",
            "data leak",
            "phishing",
            "malware",
        ],
        priority=100,
        explanation="Possible security incident detected.",
    ),
    EscalationRule(
        name="angry_or_high_risk_customer",
        queue="customer_success_review",
        triggers=[
            "angry",
            "frustrated",
            "unacceptable",
            "cancel immediately",
            "terrible service",
            "never using again",
        ],
        priority=85,
        explanation="Customer sentiment suggests high churn or reputational risk.",
    ),
    EscalationRule(
        name="enterprise_or_strategic_account",
        queue="account_manager_review",
        triggers=[
            "enterprise",
            "annual contract",
            "procurement",
            "security review",
            "large team",
            "company-wide",
        ],
        priority=90,
        explanation="Enterprise or strategic account signal detected.",
    ),
    EscalationRule(
        name="low_confidence_agent_output",
        queue="human_review",
        triggers=[],
        priority=75,
        explanation="Agent confidence is below the safe automation threshold.",
    ),
    EscalationRule(
        name="financial_exception",
        queue="finance_review",
        triggers=[
            "duplicate invoice",
            "payment mismatch",
            "overcharged",
            "refund dispute",
            "billing discrepancy",
        ],
        priority=90,
        explanation="Financial discrepancy or payment exception detected.",
    ),
]


def normalize_text(text: str) -> str:
    return text.lower().strip()


def find_trigger_matches(text: str, triggers: List[str]) -> List[str]:
    normalized = normalize_text(text)

    return [
        trigger
        for trigger in triggers
        if trigger.lower() in normalized
    ]


def evaluate_text_escalation(text: str) -> List[Dict[str, Any]]:
    """
    Evaluate escalation rules against raw request text.
    """
    matches = []

    for rule in ESCALATION_RULES:
        if not rule.triggers:
            continue

        matched_triggers = find_trigger_matches(text, rule.triggers)

        if matched_triggers:
            matches.append(
                {
                    "rule_name": rule.name,
                    "queue": rule.queue,
                    "priority": rule.priority,
                    "matched_triggers": matched_triggers,
                    "explanation": rule.explanation,
                }
            )

    return sorted(matches, key=lambda item: item["priority"], reverse=True)


def evaluate_confidence_escalation(
    confidence: Optional[float],
    threshold: float = 0.70,
) -> Optional[Dict[str, Any]]:
    """
    Escalate when confidence is below threshold.
    """
    if confidence is None:
        return {
            "rule_name": "missing_confidence",
            "queue": "human_review",
            "priority": 80,
            "matched_triggers": ["missing_confidence"],
            "explanation": "No confidence score was provided.",
        }

    if confidence < threshold:
        return {
            "rule_name": "low_confidence_agent_output",
            "queue": "human_review",
            "priority": 75,
            "matched_triggers": [f"confidence_below_{threshold}"],
            "explanation": "Agent confidence is below the safe automation threshold.",
        }

    return None


def route_escalation(
    text: str,
    confidence: Optional[float] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> EscalationDecision:
    """
    Decide whether a case should be escalated.

    Args:
        text: User request, customer message, or agent output.
        confidence: Optional agent confidence score.
        metadata: Optional structured metadata such as account type,
                  workflow name, sentiment, or risk level.
    """
    metadata = metadata or {}

    matches = evaluate_text_escalation(text)

    confidence_match = evaluate_confidence_escalation(confidence)
    if confidence_match:
        matches.append(confidence_match)

    account_type = str(metadata.get("account_type", "")).lower()
    risk_level = str(metadata.get("risk_level", "")).lower()

    if account_type in {"enterprise", "strategic"}:
        matches.append(
            {
                "rule_name": "enterprise_account_metadata",
                "queue": "account_manager_review",
                "priority": 95,
                "matched_triggers": [account_type],
                "explanation": "Enterprise or strategic account metadata requires review.",
            }
        )

    if risk_level in {"high", "critical"}:
        matches.append(
            {
                "rule_name": "high_risk_metadata",
                "queue": "human_review",
                "priority": 95,
                "matched_triggers": [risk_level],
                "explanation": "High-risk metadata requires human review.",
            }
        )

    if not matches:
        return EscalationDecision(
            should_escalate=False,
            queue=None,
            priority=0,
            matched_rules=[],
            reasons=[],
        )

    matches = sorted(matches, key=lambda item: item["priority"], reverse=True)
    top_match = matches[0]

    return EscalationDecision(
        should_escalate=True,
        queue=top_match["queue"],
        priority=top_match["priority"],
        matched_rules=[match["rule_name"] for match in matches],
        reasons=[match["explanation"] for match in matches],
    )


def format_escalation_summary(decision: EscalationDecision) -> Dict[str, Any]:
    """
    Convert an escalation decision into a serializable dictionary.
    """
    return {
        "should_escalate": decision.should_escalate,
        "queue": decision.queue,
        "priority": decision.priority,
        "matched_rules": decision.matched_rules,
        "reasons": decision.reasons,
    }

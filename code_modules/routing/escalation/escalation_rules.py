from dataclasses import dataclass, field
from typing import List, Optional


@dataclass(frozen=True)
class EscalationRule:
    name: str
    queue: str
    triggers: List[str]
    priority: int
    explanation: str
    workflows: List[str] = field(default_factory=list)
    agent_names: List[str] = field(default_factory=list)
    requires_immediate_review: bool = False
    minimum_confidence: Optional[float] = None


ESCALATION_RULES: List[EscalationRule] = [
    EscalationRule(
        name="legal_or_compliance_issue",
        queue="legal_review",
        triggers=[
            "legal",
            "lawsuit",
            "attorney",
            "contract dispute",
            "compliance",
            "regulatory",
            "gdpr",
            "hipaa",
            "data privacy",
        ],
        priority=100,
        explanation="Legal, compliance, regulatory, or data privacy concern detected.",
        requires_immediate_review=True,
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
            "compromised account",
        ],
        priority=100,
        explanation="Possible security incident or account compromise detected.",
        requires_immediate_review=True,
    ),

    EscalationRule(
        name="high_value_or_enterprise_account",
        queue="account_manager_review",
        triggers=[
            "enterprise",
            "annual contract",
            "procurement",
            "company-wide",
            "large team",
            "security questionnaire",
            "vendor review",
        ],
        priority=95,
        explanation="Enterprise, strategic, or high-value account signal detected.",
        workflows=[
            "customer_support",
            "support_to_lead",
            "lead_qualification",
        ],
    ),

    EscalationRule(
        name="angry_or_churn_risk_customer",
        queue="customer_success_review",
        triggers=[
            "angry",
            "frustrated",
            "unacceptable",
            "terrible service",
            "cancel immediately",
            "never using again",
            "switching to competitor",
        ],
        priority=85,
        explanation="Customer sentiment suggests churn, reputational risk, or urgent dissatisfaction.",
        workflows=[
            "customer_support",
            "support_to_lead",
        ],
    ),

    EscalationRule(
        name="financial_discrepancy",
        queue="finance_review",
        triggers=[
            "duplicate invoice",
            "payment mismatch",
            "overcharged",
            "refund dispute",
            "billing discrepancy",
            "incorrect charge",
            "chargeback",
        ],
        priority=90,
        explanation="Financial discrepancy, billing exception, or payment risk detected.",
        workflows=[
            "customer_support",
            "invoice_reconciliation",
        ],
    ),

    EscalationRule(
        name="employee_sensitive_issue",
        queue="hr_review",
        triggers=[
            "harassment",
            "discrimination",
            "termination",
            "disciplinary",
            "workplace complaint",
            "medical leave",
            "salary dispute",
        ],
        priority=100,
        explanation="Sensitive employee or HR-related issue detected.",
        workflows=[
            "employee_support",
        ],
        requires_immediate_review=True,
    ),

    EscalationRule(
        name="low_confidence_output",
        queue="human_review",
        triggers=[],
        priority=75,
        explanation="Agent confidence is below the safe automation threshold.",
        minimum_confidence=0.70,
    ),

    EscalationRule(
        name="missing_required_information",
        queue="human_review",
        triggers=[
            "missing required field",
            "insufficient information",
            "unclear request",
            "ambiguous intent",
            "cannot determine",
        ],
        priority=70,
        explanation="The request or agent output does not contain enough information for safe automation.",
    ),

    EscalationRule(
        name="document_answer_without_source",
        queue="knowledge_review",
        triggers=[
            "no source found",
            "missing citation",
            "unsupported answer",
            "retrieval failed",
        ],
        priority=80,
        explanation="Document or knowledge-base answer lacks adequate source support.",
        workflows=[
            "document_qa",
            "knowledge_retrieval",
        ],
    ),
]


def get_escalation_rules() -> List[EscalationRule]:
    return ESCALATION_RULES


def get_rules_for_workflow(workflow_name: str) -> List[EscalationRule]:
    return [
        rule for rule in ESCALATION_RULES
        if not rule.workflows or workflow_name in rule.workflows
    ]


def get_rules_for_agent(agent_name: str) -> List[EscalationRule]:
    return [
        rule for rule in ESCALATION_RULES
        if not rule.agent_names or agent_name in rule.agent_names
    ]


def get_immediate_review_rules() -> List[EscalationRule]:
    return [
        rule for rule in ESCALATION_RULES
        if rule.requires_immediate_review
    ]


def get_confidence_rules() -> List[EscalationRule]:
    return [
        rule for rule in ESCALATION_RULES
        if rule.minimum_confidence is not None
    ]

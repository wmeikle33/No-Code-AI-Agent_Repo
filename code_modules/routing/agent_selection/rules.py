
from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass(frozen=True)
class RoutingRule:
    name: str
    agent: str
    intents: List[str]
    keywords: List[str]
    priority: int = 50
    requires_human_review: bool = False
    explanation: str = ""
    negative_keywords: List[str] = field(default_factory=list)


ROUTING_RULES: List[RoutingRule] = [
    RoutingRule(
        name="customer_support_issue",
        agent="customer_support_agent",
        intents=[
            "technical_issue",
            "billing_question",
            "refund_request",
            "account_help",
            "product_question",
        ],
        keywords=[
            "bug",
            "error",
            "issue",
            "not working",
            "broken",
            "refund",
            "billing",
            "invoice",
            "cancel",
            "account",
            "login",
            "password",
            "support",
            "help",
        ],
        priority=80,
        explanation="Customer appears to need support, troubleshooting, billing help, or account assistance.",
    ),

    RoutingRule(
        name="lead_or_sales_opportunity",
        agent="lead_qualification_agent",
        intents=[
            "lead_qualification",
            "pricing_question",
            "demo_request",
            "upgrade_interest",
            "buying_intent",
        ],
        keywords=[
            "pricing",
            "price",
            "demo",
            "trial",
            "upgrade",
            "business plan",
            "enterprise",
            "quote",
            "sales",
            "contract",
            "buy",
            "purchase",
            "team plan",
            "usage limit",
        ],
        priority=90,
        explanation="Request contains buying intent, pricing interest, upgrade interest, or demo intent.",
    ),

    RoutingRule(
        name="support_to_lead_signal",
        agent="lead_qualification_agent",
        intents=[
            "support_to_lead",
            "upgrade_interest",
            "buying_intent",
        ],
        keywords=[
            "we are using",
            "our team",
            "usage limit",
            "need more seats",
            "business plan",
            "enterprise plan",
            "can we upgrade",
            "pricing for my team",
            "talk to sales",
        ],
        priority=95,
        explanation="Support conversation contains signals that may require a sales handoff.",
        negative_keywords=[
            "refund only",
            "cancel only",
            "delete my account",
        ],
    ),

    RoutingRule(
        name="market_research_request",
        agent="market_research_agent",
        intents=[
            "market_research",
            "competitor_analysis",
            "industry_analysis",
            "trend_analysis",
            "customer_research",
        ],
        keywords=[
            "market",
            "competitor",
            "competitors",
            "industry",
            "trend",
            "trends",
            "market size",
            "customer segment",
            "swot",
            "positioning",
            "go-to-market",
            "research brief",
        ],
        priority=75,
        explanation="Request is about market, competitor, trend, or industry research.",
    ),

    RoutingRule(
        name="document_question",
        agent="document_qa_agent",
        intents=[
            "document_question",
            "policy_question",
            "knowledge_base_lookup",
            "pdf_summary",
            "document_summary",
        ],
        keywords=[
            "document",
            "pdf",
            "file",
            "policy",
            "handbook",
            "report",
            "summarize this",
            "according to the document",
            "what does this say",
            "uploaded file",
            "knowledge base",
        ],
        priority=75,
        explanation="Request depends on a document, policy, uploaded file, or knowledge base source.",
    ),

    RoutingRule(
        name="employee_support_request",
        agent="employee_support_agent",
        intents=[
            "employee_support",
            "hr_question",
            "it_help",
            "onboarding_question",
            "benefits_question",
            "internal_policy_question",
        ],
        keywords=[
            "pto",
            "vacation",
            "benefits",
            "payroll",
            "onboarding",
            "employee",
            "hr",
            "manager approval",
            "laptop",
            "vpn",
            "internal policy",
            "expense policy",
        ],
        priority=80,
        requires_human_review=True,
        explanation="Request appears to involve internal employee, HR, IT, onboarding, or benefits support.",
    ),

    RoutingRule(
        name="executive_assistant_request",
        agent="executive_assistant_agent",
        intents=[
            "scheduling",
            "meeting_summary",
            "calendar_request",
            "task_follow_up",
            "executive_summary",
            "email_draft",
        ],
        keywords=[
            "schedule",
            "calendar",
            "meeting",
            "agenda",
            "briefing",
            "follow up",
            "action items",
            "draft email",
            "executive summary",
            "prepare notes",
            "reschedule",
        ],
        priority=70,
        explanation="Request involves scheduling, meetings, executive summaries, email drafting, or task follow-up.",
    ),

    RoutingRule(
        name="invoice_reconciliation_request",
        agent="invoice_reconciliation_agent",
        intents=[
            "invoice_reconciliation",
            "payment_check",
            "purchase_order_match",
            "expense_review",
            "billing_discrepancy",
        ],
        keywords=[
            "invoice",
            "purchase order",
            "po number",
            "receipt",
            "payment",
            "reconcile",
            "duplicate charge",
            "expense",
            "vendor",
            "billing discrepancy",
        ],
        priority=85,
        requires_human_review=True,
        explanation="Request involves invoice, purchase order, payment, vendor, or financial reconciliation.",
    ),

    RoutingRule(
        name="literature_review_request",
        agent="literature_review_agent",
        intents=[
            "literature_review",
            "paper_summary",
            "research_gap_analysis",
            "method_comparison",
            "citation_extraction",
        ],
        keywords=[
            "paper",
            "academic",
            "literature review",
            "research gap",
            "methodology",
            "citation",
            "study",
            "journal",
            "abstract",
            "related work",
        ],
        priority=75,
        explanation="Request involves academic papers, literature review, methods, citations, or research gaps.",
    ),

    RoutingRule(
        name="sensitive_or_uncertain_case",
        agent="human_review_agent",
        intents=[
            "human_review",
            "escalation",
            "sensitive_case",
            "manual_approval",
        ],
        keywords=[
            "legal",
            "compliance",
            "security breach",
            "lawsuit",
            "termination",
            "harassment",
            "medical",
            "financial risk",
            "urgent escalation",
            "human review",
        ],
        priority=100,
        requires_human_review=True,
        explanation="Request contains sensitive, high-risk, legal, compliance, or escalation signals.",
    ),
]


def normalize_text(text: str) -> str:
    """
    Normalize text for rule matching.
    """
    return text.lower().strip()


def keyword_matches(text: str, keywords: List[str]) -> List[str]:
    """
    Return keywords found in the input text.
    """
    normalized = normalize_text(text)

    return [
        keyword
        for keyword in keywords
        if keyword.lower() in normalized
    ]


def rule_matches(text: str, rule: RoutingRule) -> bool:
    """
    Check whether a routing rule matches a request.
    """
    matched_keywords = keyword_matches(text, rule.keywords)
    matched_negative_keywords = keyword_matches(text, rule.negative_keywords)

    return bool(matched_keywords) and not matched_negative_keywords


def get_matching_rules(text: str) -> List[Dict]:
    """
    Return all matching rules, ordered by priority.
    """
    matches = []

    for rule in ROUTING_RULES:
        matched_keywords = keyword_matches(text, rule.keywords)
        matched_negative_keywords = keyword_matches(text, rule.negative_keywords)

        if matched_keywords and not matched_negative_keywords:
            matches.append(
                {
                    "rule_name": rule.name,
                    "agent": rule.agent,
                    "intents": rule.intents,
                    "matched_keywords": matched_keywords,
                    "priority": rule.priority,
                    "requires_human_review": rule.requires_human_review,
                    "explanation": rule.explanation,
                }
            )

    return sorted(matches, key=lambda item: item["priority"], reverse=True)


def get_best_rule_match(text: str) -> Optional[Dict]:
    """
    Return the highest-priority rule match.
    """
    matches = get_matching_rules(text)

    if not matches:
        return None

    return matches[0]


def suggest_agent_from_rules(text: str) -> Dict:
    """
    Suggest an agent using only rule-based routing.
    """
    best_match = get_best_rule_match(text)

    if not best_match:
        return {
            "agent": "general_assistant_agent",
            "confidence": 0.4,
            "source": "rules",
            "matched_rule": None,
            "requires_human_review": False,
            "explanation": "No specific routing rule matched. Using general assistant fallback.",
        }

    confidence = min(0.95, 0.55 + (best_match["priority"] / 100) * 0.4)

    return {
        "agent": best_match["agent"],
        "confidence": round(confidence, 2),
        "source": "rules",
        "matched_rule": best_match["rule_name"],
        "matched_keywords": best_match["matched_keywords"],
        "requires_human_review": best_match["requires_human_review"],
        "explanation": best_match["explanation"],
    }

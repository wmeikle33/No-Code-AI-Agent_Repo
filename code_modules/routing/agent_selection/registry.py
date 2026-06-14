
from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass(frozen=True)
class AgentDefinition:
    name: str
    display_name: str
    description: str
    primary_intents: List[str]
    supported_workflows: List[str]
    capabilities: List[str]
    fallback_agent: Optional[str] = None
    requires_human_review: bool = False
    tags: List[str] = field(default_factory=list)


AGENT_REGISTRY: Dict[str, AgentDefinition] = {
    "customer_support_agent": AgentDefinition(
        name="customer_support_agent",
        display_name="Customer Support Agent",
        description="Handles customer questions, troubleshooting, billing issues, refunds, and support ticket triage.",
        primary_intents=[
            "customer_support",
            "technical_issue",
            "billing_question",
            "refund_request",
            "account_help",
            "product_question",
        ],
        supported_workflows=[
            "customer_support",
            "support_to_lead",
        ],
        capabilities=[
            "classify_support_request",
            "answer_customer_question",
            "detect_escalation_need",
            "summarize_support_case",
            "identify_sales_opportunity",
        ],
        fallback_agent="human_review_agent",
        tags=["support", "customer-facing", "triage"],
    ),

    "lead_qualification_agent": AgentDefinition(
        name="lead_qualification_agent",
        display_name="Lead Qualification Agent",
        description="Evaluates sales intent, qualifies leads, scores opportunities, and prepares sales handoff notes.",
        primary_intents=[
            "lead_qualification",
            "pricing_question",
            "demo_request",
            "upgrade_interest",
            "sales_handoff",
            "buying_intent",
        ],
        supported_workflows=[
            "lead_qualification",
            "support_to_lead",
        ],
        capabilities=[
            "score_lead",
            "detect_buying_signals",
            "classify_lead_temperature",
            "generate_sales_handoff",
            "recommend_follow_up_action",
        ],
        fallback_agent="human_review_agent",
        tags=["sales", "crm", "qualification"],
    ),

    "market_research_agent": AgentDefinition(
        name="market_research_agent",
        display_name="Market Research Agent",
        description="Performs market, competitor, trend, customer, and industry research.",
        primary_intents=[
            "market_research",
            "competitor_analysis",
            "industry_analysis",
            "trend_analysis",
            "customer_research",
        ],
        supported_workflows=[
            "market_research",
            "competitive_analysis",
        ],
        capabilities=[
            "summarize_market_trends",
            "compare_competitors",
            "identify_market_opportunities",
            "generate_research_brief",
            "extract_key_findings",
        ],
        fallback_agent="research_review_agent",
        tags=["research", "strategy", "analysis"],
    ),

    "document_qa_agent": AgentDefinition(
        name="document_qa_agent",
        display_name="Document Q&A Agent",
        description="Answers questions using uploaded documents, policies, PDFs, reports, and internal knowledge sources.",
        primary_intents=[
            "document_question",
            "policy_question",
            "knowledge_base_lookup",
            "pdf_summary",
            "document_summary",
        ],
        supported_workflows=[
            "document_qa",
            "knowledge_retrieval",
        ],
        capabilities=[
            "retrieve_relevant_context",
            "answer_from_documents",
            "summarize_document",
            "cite_sources",
            "detect_missing_context",
        ],
        fallback_agent="human_review_agent",
        tags=["rag", "documents", "knowledge-base"],
    ),

    "employee_support_agent": AgentDefinition(
        name="employee_support_agent",
        display_name="Employee Support Agent",
        description="Handles internal employee questions about HR, IT, onboarding, benefits, and company policies.",
        primary_intents=[
            "employee_support",
            "hr_question",
            "it_help",
            "onboarding_question",
            "benefits_question",
            "internal_policy_question",
        ],
        supported_workflows=[
            "employee_support",
        ],
        capabilities=[
            "answer_internal_question",
            "route_hr_request",
            "route_it_request",
            "summarize_employee_issue",
            "detect_sensitive_request",
        ],
        fallback_agent="human_review_agent",
        requires_human_review=True,
        tags=["internal", "hr", "it", "employee"],
    ),

    "executive_assistant_agent": AgentDefinition(
        name="executive_assistant_agent",
        display_name="Executive Assistant Agent",
        description="Helps with scheduling, meeting preparation, summaries, task follow-up, and executive communication.",
        primary_intents=[
            "scheduling",
            "meeting_summary",
            "calendar_request",
            "task_follow_up",
            "executive_summary",
            "email_draft",
        ],
        supported_workflows=[
            "executive_assistant",
            "meeting_notes",
        ],
        capabilities=[
            "summarize_meeting",
            "draft_email",
            "prepare_briefing",
            "extract_action_items",
            "prioritize_tasks",
        ],
        fallback_agent="human_review_agent",
        tags=["productivity", "executive", "communication"],
    ),

    "invoice_reconciliation_agent": AgentDefinition(
        name="invoice_reconciliation_agent",
        display_name="Invoice Reconciliation Agent",
        description="Compares invoices, purchase orders, receipts, and payment records to identify mismatches.",
        primary_intents=[
            "invoice_reconciliation",
            "payment_check",
            "purchase_order_match",
            "expense_review",
            "billing_discrepancy",
        ],
        supported_workflows=[
            "invoice_reconciliation",
        ],
        capabilities=[
            "compare_invoice_to_po",
            "detect_payment_mismatch",
            "flag_duplicate_invoice",
            "summarize_financial_exception",
            "prepare_review_note",
        ],
        fallback_agent="human_review_agent",
        requires_human_review=True,
        tags=["finance", "operations", "compliance"],
    ),

    "literature_review_agent": AgentDefinition(
        name="literature_review_agent",
        display_name="Literature Review Agent",
        description="Reviews academic papers, summarizes findings, compares methods, and extracts research gaps.",
        primary_intents=[
            "literature_review",
            "paper_summary",
            "research_gap_analysis",
            "method_comparison",
            "citation_extraction",
        ],
        supported_workflows=[
            "literature_review",
            "research_synthesis",
        ],
        capabilities=[
            "summarize_paper",
            "compare_research_methods",
            "extract_limitations",
            "identify_research_gaps",
            "generate_literature_matrix",
        ],
        fallback_agent="research_review_agent",
        tags=["academic", "research", "papers"],
    ),

    "human_review_agent": AgentDefinition(
        name="human_review_agent",
        display_name="Human Review Agent",
        description="Represents a human-in-the-loop review step for uncertain, sensitive, high-risk, or low-confidence cases.",
        primary_intents=[
            "human_review",
            "escalation",
            "low_confidence",
            "sensitive_case",
            "manual_approval",
        ],
        supported_workflows=[
            "customer_support",
            "support_to_lead",
            "employee_support",
            "invoice_reconciliation",
            "document_qa",
        ],
        capabilities=[
            "flag_for_manual_review",
            "prepare_review_summary",
            "explain_routing_uncertainty",
            "recommend_next_action",
        ],
        tags=["fallback", "review", "safety"],
    ),

    "general_assistant_agent": AgentDefinition(
        name="general_assistant_agent",
        display_name="General Assistant Agent",
        description="Handles general requests that do not clearly belong to a specialized agent.",
        primary_intents=[
            "general_question",
            "unclear_request",
            "miscellaneous",
        ],
        supported_workflows=[
            "general_assistance",
        ],
        capabilities=[
            "clarify_request",
            "provide_general_answer",
            "suggest_best_agent",
            "route_to_specialist",
        ],
        fallback_agent="human_review_agent",
        tags=["general", "fallback", "clarification"],
    ),
}


def get_agent(agent_name: str) -> Optional[AgentDefinition]:
    """
    Return a single agent definition by name.
    """
    return AGENT_REGISTRY.get(agent_name)


def list_agents() -> List[str]:
    """
    Return all registered agent names.
    """
    return list(AGENT_REGISTRY.keys())


def get_agents_for_intent(intent: str) -> List[AgentDefinition]:
    """
    Return agents that support a given intent.
    """
    return [
        agent
        for agent in AGENT_REGISTRY.values()
        if intent in agent.primary_intents
    ]


def get_agents_for_workflow(workflow_name: str) -> List[AgentDefinition]:
    """
    Return agents that participate in a given workflow.
    """
    return [
        agent
        for agent in AGENT_REGISTRY.values()
        if workflow_name in agent.supported_workflows
    ]


def get_fallback_agent(agent_name: str) -> Optional[AgentDefinition]:
    """
    Return the fallback agent for a given agent.
    """
    agent = get_agent(agent_name)

    if not agent or not agent.fallback_agent:
        return None

    return get_agent(agent.fallback_agent)


def agent_supports_intent(agent_name: str, intent: str) -> bool:
    """
    Check whether an agent supports a specific intent.
    """
    agent = get_agent(agent_name)

    if not agent:
        return False

    return intent in agent.primary_intents


def agent_supports_workflow(agent_name: str, workflow_name: str) -> bool:
    """
    Check whether an agent supports a specific workflow.
    """
    agent = get_agent(agent_name)

    if not agent:
        return False

    return workflow_name in agent.supported_workflows


def search_agents_by_tag(tag: str) -> List[AgentDefinition]:
    """
    Return agents matching a specific tag.
    """
    return [
        agent
        for agent in AGENT_REGISTRY.values()
        if tag in agent.tags

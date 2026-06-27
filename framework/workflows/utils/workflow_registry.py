AGENT_REGISTRY = {
    "customer_support": {
        "description": "Handles customer issues, refunds, troubleshooting, and support tickets.",
        "tools": ["knowledge_search", "ticket_lookup"]
    },
    "lead_qualification": {
        "description": "Scores and qualifies sales leads.",
        "tools": ["crm_lookup"]
    },
    "document_qa": {
        "description": "Answers questions using uploaded documents.",
        "tools": ["knowledge_search"]
    }
}


def get_agent(agent_name: str) -> dict:
    if agent_name not in AGENT_REGISTRY:
        raise ValueError(f"Unknown agent: {agent_name}")
    return AGENT_REGISTRY[agent_name]

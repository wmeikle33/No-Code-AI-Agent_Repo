def route_request(user_request: str) -> str:
    text = user_request.lower()

    if any(word in text for word in ["refund", "ticket", "support", "problem", "issue"]):
        return "customer_support"

    if any(word in text for word in ["lead", "prospect", "sales", "qualify"]):
        return "lead_qualification"

    if any(word in text for word in ["document", "policy", "file", "pdf"]):
        return "document_qa"

    return "customer_support"

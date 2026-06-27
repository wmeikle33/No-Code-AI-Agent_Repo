def audit_internal_policies_against_laws(policy_document_path, latest_laws_text):
    with open(policy_document_path, "r", encoding="utf-8") as file:
        policy_text = file.read()

    missing_terms = []

    for keyword in ["minimum wage", "overtime", "leave", "harassment", "discrimination", "termination"]:
        if keyword in latest_laws_text.lower() and keyword not in policy_text.lower():
            missing_terms.append(keyword)

    return {
        "policy_document_path": policy_document_path,
        "missing_policy_topics": missing_terms,
        "requires_human_legal_review": True
    }

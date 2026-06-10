def create_lead(name: str, email: str, interest: str) -> dict:
    if not name:
        raise ValueError("Lead name is required")

    if not email or "@" not in email:
        raise ValueError("Valid email is required")

    if not interest:
        raise ValueError("Lead interest is required")

    return {
        "status": "created",
        "lead": {
            "name": name,
            "email": email,
            "interest": interest,
            "source": "customer_support_agent",
        },
    }

def create_lead(name: str, email: str, interest: str) -> dict:
    return {
        "status": "created",
        "lead": {
            "name": name,
            "email": email,
            "interest": interest,
            "source": "customer_support_agent"
        }
    }

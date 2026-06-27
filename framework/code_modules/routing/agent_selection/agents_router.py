def select_agent(user_input: dict) -> str:
    if user_input["type"] == "support":
        return "customer_support_agent"

    if user_input["type"] == "sales":
        return "sales_agent"

    return "general_agent"

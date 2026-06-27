def run_tool(tool_name: str, user_request: str) -> dict:
    if tool_name == "knowledge_search":
        return {
            "tool": tool_name,
            "result": "Mock knowledge result related to the user request."
        }

    if tool_name == "ticket_lookup":
        return {
            "tool": tool_name,
            "result": "Mock ticket data."
        }

    if tool_name == "crm_lookup":
        return {
            "tool": tool_name,
            "result": "Mock CRM lead data."
        }

    return {
        "tool": tool_name,
        "result": None,
        "error": f"Unknown tool: {tool_name}"
    }

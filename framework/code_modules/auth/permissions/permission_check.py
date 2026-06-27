def can_execute_tool(
    role: str,
    tool_name: str
) -> bool:

    if role == "admin":
        return True

    if tool_name == "delete_database":
        return False

    return True

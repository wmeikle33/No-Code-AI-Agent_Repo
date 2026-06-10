def validate_api_key(api_key: str) -> bool:
    if not api_key:
        return False

    if len(api_key) < 20:
        return False

    return True

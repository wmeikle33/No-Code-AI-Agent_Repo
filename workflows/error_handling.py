def format_error(error: Exception) -> dict:
    return {
        "status": "error",
        "message": str(error)
    }

def check_human_review(user_request: str, final_output: dict) -> bool:
    risky_words = ["refund", "legal", "medical", "fire", "terminate", "payment"]

    text = user_request.lower()

    return any(word in text for word in risky_words)

def analyze_survey_sentiment(survey_responses_list):
    positive_words = {"good", "great", "happy", "supported", "clear", "fair", "excellent"}
    negative_words = {"bad", "poor", "stress", "unclear", "unfair", "burned", "frustrated"}

    scores = []

    for response in survey_responses_list:
        words = set(re.findall(r"\w+", response.lower()))
        score = len(words & positive_words) - len(words & negative_words)
        scores.append(score)

    avg_score = mean(scores) if scores else 0

    if avg_score > 0:
        sentiment = "positive"
    elif avg_score < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return {
        "response_count": len(survey_responses_list),
        "average_score": avg_score,
        "overall_sentiment": sentiment
    }

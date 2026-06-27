def predict_ammonia_accumulation_trends(historical_sensor_data):
    ammonia_values = [row["ammonia_ppm"] for row in historical_sensor_data if "ammonia_ppm" in row]

    if len(ammonia_values) < 2:
        return {"trend": "insufficient_data"}

    change = ammonia_values[-1] - ammonia_values[0]

    if change > 0.2:
        trend = "increasing"
    elif change < -0.2:
        trend = "decreasing"
    else:
        trend = "stable"

    return {
        "trend": trend,
        "first_value": ammonia_values[0],
        "latest_value": ammonia_values[-1],
        "average_value": mean(ammonia_values)
    }

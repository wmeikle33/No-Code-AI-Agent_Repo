def optimize_feed_to_biomass_ratio(water_temp, fish_age, population_count):
    base_feed_rate = 0.02

    if water_temp < 18:
        temp_modifier = 0.7
    elif water_temp > 28:
        temp_modifier = 0.8
    else:
        temp_modifier = 1.0

    if fish_age < 30:
        age_modifier = 1.3
    elif fish_age > 180:
        age_modifier = 0.8
    else:
        age_modifier = 1.0

    return {
        "estimated_feed_rate_percent_body_weight": round(base_feed_rate * temp_modifier * age_modifier * 100, 2),
        "population_count": population_count,
        "note": "Requires actual biomass weight for production-grade feed calculation."
    }

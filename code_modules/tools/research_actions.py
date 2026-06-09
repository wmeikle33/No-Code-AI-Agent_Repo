from statistics import mean
from collections import Counter
import re


def research_market_salaries(job_title, location, experience_level):
    base_salary = {
        "junior": 65000,
        "mid": 90000,
        "senior": 125000,
        "lead": 150000
    }

    salary = base_salary.get(experience_level.lower(), 90000)

    return {
        "job_title": job_title,
        "location": location,
        "experience_level": experience_level,
        "estimated_market_range": {
            "low": int(salary * 0.85),
            "median": salary,
            "high": int(salary * 1.2)
        },
        "source_type": "mock_market_research",
        "recommendation": "Replace this mock logic with a salary API or scraped compensation dataset."
    }


def compare_internal_vs_market_pay(employee_id):
    internal_salary = 88000
    market_median = 95000
    gap = internal_salary - market_median

    return {
        "employee_id": employee_id,
        "internal_salary": internal_salary,
        "market_median_salary": market_median,
        "pay_gap": gap,
        "pay_position": "below_market" if gap < 0 else "at_or_above_market",
        "recommendation": "Review compensation adjustment if employee is high-performing or flight-risk."
    }


def analyze_survey_sentiment(survey_responses_list):
    positive_words = {"good", "great", "happy", "supported", "clear", "fair", "positive"}
    negative_words = {"bad", "poor", "unclear", "stress", "stressed", "unfair", "negative", "burnout"}

    results = []

    for response in survey_responses_list:
        words = set(response.lower().split())
        positive_score = len(words & positive_words)
        negative_score = len(words & negative_words)

        if positive_score > negative_score:
            sentiment = "positive"
        elif negative_score > positive_score:
            sentiment = "negative"
        else:
            sentiment = "neutral"

        results.append({
            "response": response,
            "sentiment": sentiment,
            "positive_score": positive_score,
            "negative_score": negative_score
        })

    sentiment_counts = Counter(item["sentiment"] for item in results)

    return {
        "total_responses": len(survey_responses_list),
        "sentiment_summary": dict(sentiment_counts),
        "response_analysis": results
    }


def extract_key_feedback_themes(department_name):
    mock_themes = {
        "engineering": ["workload", "technical debt", "career growth", "meeting overload"],
        "sales": ["commission structure", "lead quality", "quota pressure", "CRM friction"],
        "hr": ["policy clarity", "onboarding", "employee engagement", "benefits"]
    }

    return {
        "department": department_name,
        "key_themes": mock_themes.get(department_name.lower(), ["communication", "workload", "manager support"]),
        "recommendation": "Use real survey or interview text for production theme extraction."
    }


def check_labor_law_updates(state_or_country):
    return {
        "jurisdiction": state_or_country,
        "status": "mock_update",
        "updates_found": [
            "Minimum wage requirements may need review.",
            "Pay transparency rules may apply.",
            "Leave policy requirements may have changed."
        ],
        "recommendation": "Connect this to an official labor-law source or legal database before production use."
    }


def audit_internal_policies_against_laws(policy_document_path, latest_laws_text):
    try:
        with open(policy_document_path, "r", encoding="utf-8") as file:
            policy_text = file.read()
    except FileNotFoundError:
        return {
            "status": "error",
            "message": f"Policy document not found: {policy_document_path}"
        }

    issues = []

    if "minimum wage" in latest_laws_text.lower() and "minimum wage" not in policy_text.lower():
        issues.append("Policy may be missing minimum wage language.")

    if "leave" in latest_laws_text.lower() and "leave" not in policy_text.lower():
        issues.append("Policy may be missing leave-policy language.")

    if "pay transparency" in latest_laws_text.lower() and "pay transparency" not in policy_text.lower():
        issues.append("Policy may be missing pay transparency language.")

    return {
        "policy_document_path": policy_document_path,
        "issues_found": issues,
        "compliance_status": "review_needed" if issues else "no_obvious_gaps_found",
        "disclaimer": "This is not legal advice. Human legal review is required."
    }


def analyze_talent_scarcity(skill_keywords, location):
    scarcity_scores = {}

    for skill in skill_keywords:
        skill_lower = skill.lower()

        if skill_lower in {"ai", "machine learning", "ml", "cybersecurity", "data engineering"}:
            score = "high"
        elif skill_lower in {"python", "sql", "project management"}:
            score = "medium"
        else:
            score = "unknown"

        scarcity_scores[skill] = score

    return {
        "location": location,
        "skill_scarcity": scarcity_scores,
        "recommendation": "Prioritize compensation benchmarking and proactive sourcing for high-scarcity skills."
    }


def summarize_competitor_job_postings(competitor_name):
    return {
        "competitor": competitor_name,
        "summary": {
            "common_roles": ["Software Engineer", "Product Manager", "Data Analyst"],
            "common_benefits": ["remote work", "health insurance", "equity", "learning stipend"],
            "hiring_signals": "Moderate hiring activity based on mock data."
        },
        "recommendation": "Replace mock data with job board, LinkedIn, or company careers-page scraping."
    }


def predict_turnover_risk_factors():
    return {
        "top_risk_factors": [
            "below-market compensation",
            "low manager support",
            "limited career progression",
            "high workload",
            "low engagement survey scores"
        ],
        "recommended_actions": [
            "Review compensation bands",
            "Identify teams with high workload",
            "Improve promotion-path clarity",
            "Conduct stay interviews"
        ]
    }


def research_water_chemistry_bounds(fish_species, plant_species):
    return {
        "fish_species": fish_species,
        "plant_species": plant_species,
        "recommended_bounds": {
            "ph": "6.8 - 7.2",
            "ammonia_ppm": "0 - 0.25",
            "nitrite_ppm": "0 - 0.5",
            "nitrate_ppm": "20 - 80",
            "water_temperature_c": "20 - 28"
        },
        "note": "Use species-specific aquaculture references before production deployment."
    }


def predict_ammonia_accumulation_trends(historical_sensor_data):
    ammonia_values = [row["ammonia_ppm"] for row in historical_sensor_data if "ammonia_ppm" in row]

    if len(ammonia_values) < 2:
        return {
            "trend": "insufficient_data",
            "recommendation": "Collect more sensor readings."
        }

    change = ammonia_values[-1] - ammonia_values[0]

    if change > 0.2:
        trend = "rising"
    elif change < -0.2:
        trend = "falling"
    else:
        trend = "stable"

    return {
        "starting_ammonia": ammonia_values[0],
        "latest_ammonia": ammonia_values[-1],
        "average_ammonia": round(mean(ammonia_values), 3),
        "trend": trend,
        "recommendation": "Check filtration and feeding levels if ammonia is rising."
    }


def evaluate_ecosystem_compatibility(fish_type, plant_type):
    compatible_pairs = {
        ("tilapia", "lettuce"),
        ("tilapia", "basil"),
        ("trout", "lettuce"),
        ("goldfish", "herbs")
    }

    pair = (fish_type.lower(), plant_type.lower())

    return {
        "fish_type": fish_type,
        "plant_type": plant_type,
        "compatible": pair in compatible_pairs,
        "recommendation": "Validate temperature, pH, and nutrient needs before deployment."
    }


def calculate_supplementary_nutrient_dosing(plant_deficiency_logs):
    dosing_plan = []

    for log in plant_deficiency_logs:
        deficiency = log.get("deficiency", "").lower()

        if "iron" in deficiency:
            recommendation = "Add chelated iron according to product label."
        elif "potassium" in deficiency:
            recommendation = "Consider potassium supplementation."
        elif "calcium" in deficiency:
            recommendation = "Consider calcium supplementation."
        else:
            recommendation = "Monitor and confirm deficiency before dosing."

        dosing_plan.append({
            "plant_id": log.get("plant_id"),
            "deficiency": log.get("deficiency"),
            "recommendation": recommendation
        })

    return {
        "dosing_plan": dosing_plan,
        "warning": "Avoid overdosing. Confirm with water testing before adding nutrients."
    }


def analyze_plant_canopy_health(camera_image_path):
    return {
        "camera_image_path": camera_image_path,
        "health_status": "mock_analysis_complete",
        "observations": [
            "Canopy density appears acceptable.",
            "No image model is currently connected.",
            "Future version can use computer vision for yellowing, wilting, or pest detection."
        ]
    }


def monitor_fish_behavior_anomalies(video_stream_sample):
    return {
        "video_stream_sample": video_stream_sample,
        "anomaly_status": "mock_analysis_complete",
        "detected_anomalies": [],
        "recommendation": "Connect to a video model or motion-tracking system for real anomaly detection."
    }


def optimize_feed_to_biomass_ratio(water_temp, fish_age, population_count):
    base_feed_grams_per_fish = 3

    if water_temp < 18:
        temp_adjustment = 0.75
    elif water_temp > 28:
        temp_adjustment = 0.85
    else:
        temp_adjustment = 1.0

    if fish_age < 30:
        age_adjustment = 0.6
    elif fish_age > 180:
        age_adjustment = 1.2
    else:
        age_adjustment = 1.0

    daily_feed = population_count * base_feed_grams_per_fish * temp_adjustment * age_adjustment

    return {
        "water_temp": water_temp,
        "fish_age_days": fish_age,
        "population_count": population_count,
        "recommended_daily_feed_grams": round(daily_feed, 2),
        "recommendation": "Adjust based on observed feeding behavior and water-quality readings."
    }


def calculate_operational_roi(energy_tariff_rates, crop_market_prices):
    monthly_energy_cost = sum(energy_tariff_rates)
    projected_crop_revenue = sum(crop_market_prices)
    roi = projected_crop_revenue - monthly_energy_cost

    return {
        "monthly_energy_cost": round(monthly_energy_cost, 2),
        "projected_crop_revenue": round(projected_crop_revenue, 2),
        "estimated_net_return": round(roi, 2),
        "roi_status": "positive" if roi > 0 else "negative"
    }

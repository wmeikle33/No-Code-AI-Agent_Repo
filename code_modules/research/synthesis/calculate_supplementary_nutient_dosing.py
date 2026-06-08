
def calculate_supplementary_nutrient_dosing(plant_deficiency_logs):
    recommendations = []

    for log in plant_deficiency_logs:
        deficiency = log.get("deficiency", "").lower()

        if "iron" in deficiency:
            recommendations.append("consider chelated iron")
        elif "potassium" in deficiency:
            recommendations.append("consider potassium supplement")
        elif "calcium" in deficiency:
            recommendations.append("consider calcium supplement")

    return {
        "recommendations": sorted(set(recommendations)),
        "requires_expert_review": True
    }


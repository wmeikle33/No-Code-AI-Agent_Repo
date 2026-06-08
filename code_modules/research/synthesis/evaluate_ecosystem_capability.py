def evaluate_ecosystem_compatibility(fish_type, plant_type):
    return {
        "fish_type": fish_type,
        "plant_type": plant_type,
        "compatibility": "requires_species_database",
        "checks": [
            "temperature overlap",
            "pH overlap",
            "nutrient demand",
            "growth cycle timing",
            "stocking density"
        ]
    }

def research_water_chemistry_bounds(fish_species, plant_species):
    return {
        "fish_species": fish_species,
        "plant_species": plant_species,
        "recommended_bounds": {
            "ph": {"min": 6.5, "max": 7.2},
            "ammonia_ppm": {"max": 0.5},
            "nitrite_ppm": {"max": 1.0},
            "nitrate_ppm": {"min": 5, "max": 150},
            "temperature_c": {"min": 18, "max": 28}
        },
        "note": "Use species-specific aquaculture and horticulture references before production use."
    }

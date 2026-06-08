def calculate_operational_roi(energy_tariff_rates, crop_market_prices):
    average_energy_rate = mean(energy_tariff_rates) if energy_tariff_rates else 0
    average_crop_price = mean(crop_market_prices) if crop_market_prices else 0

    return {
        "average_energy_rate": average_energy_rate,
        "average_crop_price": average_crop_price,
        "roi_status": "requires cost, yield, labor, equipment, and revenue data"
    }

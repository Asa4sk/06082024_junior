car_4x2 = {
    "price": 800000,
    "is_rear_led_lights_dynamic_indicators": True,
    "exterior_design_features": [
        "chrome grille",
        "17-inch alloy wheels",
        "LED headlights",
        "roof rails",
        "daytime running lights",
    ],
    "panoramic_sunroof": {},
    "has_parking_sensors": True,
    "has_climate_control": True,
    "has_multimedia_display": True,
    "engine_power": 171,
    "transmission": "CVT",
    "drive": "4x2",
    "fuel_type": "gasoline",
}


car_4x4_intense = {
    "price": 950000,
    "is_rear_led_lights_dynamic_indicators": True,
    "exterior_design_features": [
        "chrome grille",
        "19-inch alloy wheels",
        "LED headlights",
        "roof rails",
        "daytime running lights",
        "fog lights",
    ],
    "panoramic_sunroof": {"price": 25000},
    "has_parking_sensors": True,
    "has_climate_control": True,
    "has_multimedia_display": True,
    "engine_power": 171,
    "transmission": "CVT",
    "drive": "4x4",
    "fuel_type": "gasoline",
}
panoramic_price_4x4 = car_4x4_intense["panoramic_sunroof"].get("price", "Not available")
print(f"Panoramic sunroof price for 4x4: {panoramic_price_4x4}")

exterior_features_4x4 = car_4x4_intense["exterior_design_features"]
print("Exterior design features for 4x4:")
for feature in exterior_features_4x4:
    print(f"- {feature}")

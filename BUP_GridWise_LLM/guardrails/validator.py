def validate_energy_data(
    current_load: float,
    solar_generation: float,
    battery_level: float
):
    """
    Validate energy-related input values.
    """

    if current_load < 0:
        return False, "Current load cannot be negative."

    if solar_generation < 0:
        return False, "Solar generation cannot be negative."

    if battery_level < 0 or battery_level > 100:
        return False, "Battery level must be between 0 and 100."

    return True, "Energy data is valid."
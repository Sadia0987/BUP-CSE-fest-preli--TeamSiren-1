def optimize_energy(
    current_load: float,
    solar_generation: float,
    battery_level: float
):
    """
    Simple energy optimization logic.
    """

    # Solar power used first
    solar_used = min(current_load, solar_generation)

    # Load remaining after using solar
    remaining_load = current_load - solar_used

    # Case 1: Solar can cover the full load
    if remaining_load <= 0:
        action = "Use solar power"
        saving = current_load
        message = (
            "Solar generation can cover the current load."
        )

    # Case 2: Battery is high
    elif battery_level > 50:
        action = "Use battery backup"
        saving = solar_used
        message = (
            "Use available solar power first, "
            "then battery backup."
        )

    # Case 3: Battery is moderate
    elif battery_level > 20:
        action = "Reduce non-essential load"
        saving = solar_used
        message = (
            "Battery level is moderate. "
            "Reduce unnecessary consumption."
        )

    # Case 4: Battery is low
    else:
        action = "Minimize energy consumption"
        saving = solar_used
        message = (
            "Battery level is low. "
            "Minimize non-essential energy usage."
        )

    return {
        "recommended_action": action,
        "estimated_saving": round(saving, 2),
        "remaining_load": round(remaining_load, 2),
        "message": message
    }
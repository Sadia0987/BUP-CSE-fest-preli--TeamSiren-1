import re


def interpret_query(question: str):
    """
    Convert a natural-language energy query
    into structured energy information.
    """

    text = question.lower()

    current_load = None
    solar_generation = None
    battery_level = None

    # Current load
    load_match = re.search(
        r"(\d+(?:\.\d+)?)\s*k?w?\s*(?:of\s+)?(?:current\s+)?load",
        text
    )

    if load_match:
        current_load = float(load_match.group(1))

    # Solar generation
    solar_match = re.search(
        r"(\d+(?:\.\d+)?)\s*k?w?\s*solar(?:\s+generation|\s+power)?",
        text
    )

    if solar_match:
        solar_generation = float(solar_match.group(1))

    # Battery
    battery_match = re.search(
        r"(\d+(?:\.\d+)?)\s*%?\s*battery",
        text
    )

    if battery_match:
        battery_level = float(battery_match.group(1))

    return {
        "current_load": current_load,
        "solar_generation": solar_generation,
        "battery_level": battery_level,
        "original_question": question
    }
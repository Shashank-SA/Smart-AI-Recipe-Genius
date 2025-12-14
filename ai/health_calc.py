def calculate_health_report(vegetables):
    """
    Returns a standardized health report dictionary.
    This function NEVER throws KeyError.
    """

    if not vegetables:
        return {
            "calories": 0,
            "score": 0,
            "level": "Unknown"
        }

    # Simple heuristic (safe & explainable in viva)
    calories = len(vegetables) * 50

    if calories < 150:
        score = 85
        level = "Very Healthy"
    elif calories < 300:
        score = 70
        level = "Healthy"
    else:
        score = 55
        level = "Moderate"

    return {
        "calories": calories,
        "score": score,
        "level": level
    }

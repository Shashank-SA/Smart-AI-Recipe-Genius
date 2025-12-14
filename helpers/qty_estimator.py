import math

# Basic per-person quantity estimates (approx)
BASE_QUANTITIES = {
    "tomato": 1,
    "onion": 1,
    "potato": 1,
    "carrot": 1,
    "capsicum": 0.5,
    "spinach": 50,     # grams
    "cabbage": 100,    # grams
    "cauliflower": 100,
    "beans": 50,
    "peas": 50,
    "brinjal": 1,
    "garlic": 2,       # cloves
    "ginger": 1,       # inch
}

DEFAULT_UNIT = {
    "tomato": "piece",
    "onion": "piece",
    "potato": "piece",
    "carrot": "piece",
    "capsicum": "piece",
    "spinach": "grams",
    "cabbage": "grams",
    "cauliflower": "grams",
    "beans": "grams",
    "peas": "grams",
    "brinjal": "piece",
    "garlic": "cloves",
    "ginger": "inch",
}


def estimate_quantities(ingredients, servings=2):
    """
    Estimate ingredient quantities based on servings.

    Args:
        ingredients (list): list of ingredient names
        servings (int): number of people

    Returns:
        list: formatted ingredient strings with quantities
    """

    if not ingredients:
        return []

    servings = max(1, servings)
    estimated = []

    for item in ingredients:
        name = item.lower().strip()

        base_qty = BASE_QUANTITIES.get(name)
        unit = DEFAULT_UNIT.get(name, "")

        if base_qty:
            qty = base_qty * servings

            # Round nicely
            if unit in ["grams"]:
                qty = int(math.ceil(qty / 10.0) * 10)
            else:
                qty = math.ceil(qty)

            estimated.append(f"{qty} {unit} {name}")
        else:
            # Unknown ingredient fallback
            estimated.append(f"{name} (as required)")

    return estimated

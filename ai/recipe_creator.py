from ai.llm_api import generate_recipe_instructions


def create_recipe(recipe_name, vegetables):
    try:
        return generate_recipe_instructions(recipe_name, vegetables)
    except Exception as e:
        return f"Error generating recipe: {e}"


def create_shopping_list(recipe_text):
    lines = recipe_text.split("\n")
    ingredients = []
    capture = False

    for line in lines:
        line = line.strip().lower()

        if "ingredients" in line:
            capture = True
            continue

        if "steps" in line or "instructions" in line:
            break

        if capture:
            if line.startswith(("-", "•", "*")):
                ingredients.append(line.lstrip("-•* ").strip())
            elif line:
                ingredients.append(line)

    return ingredients if ingredients else ["No ingredients detected"]

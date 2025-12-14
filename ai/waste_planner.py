from ai.llm_api import call_llm


def generate_waste_reduction_tips(vegetables):
    if not vegetables:
        return ["No vegetables detected"]

    prompt = f"""
    Vegetables available: {", ".join(vegetables)}.
    Give 5 simple food waste reduction tips.
    One tip per line.
    """

    try:
        response = call_llm(prompt)
    except Exception as e:
        return [str(e)]

    tips = []
    for line in response.split("\n"):
        line = line.strip("-•* ").strip()
        if line:
            tips.append(line)

    return tips

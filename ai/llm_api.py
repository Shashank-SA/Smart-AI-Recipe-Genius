import requests
import streamlit as st

GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

MODEL = "llama-3.1-8b-instant"   # free, fast, reliable
API_URL = "https://api.groq.com/openai/v1/chat/completions"


def call_llm(prompt: str):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3,
        "max_tokens": 1200
    }

    response = requests.post(API_URL, headers=headers, json=payload, timeout=30)

    if response.status_code != 200:
        raise Exception(f"GROQ Error {response.status_code}: {response.text}")

    return response.json()["choices"][0]["message"]["content"]


# ----------------------------
# RECIPE NAME GENERATION
# ----------------------------
def generate_recipe_names(vegetables):
    prompt = f"""
    I have the following vegetables: {", ".join(vegetables)}.
    Suggest 5 creative recipe names in different cuisines.
    Return ONLY the names, one per line.
    """
    return call_llm(prompt)


# ----------------------------
# FULL RECIPE GENERATION
# ----------------------------
def generate_recipe_instructions(recipe_name, vegetables):
    prompt = f"""
    Create a detailed cooking recipe for: {recipe_name}.

    Available vegetables: {", ".join(vegetables)}.

    Use this exact format:
    Recipe Name:
    Description:
    Ingredients:
    - item
    Steps:
    1. step
    Cooking Time:
    Servings:
    """
    return call_llm(prompt)

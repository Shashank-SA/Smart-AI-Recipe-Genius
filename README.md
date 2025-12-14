# Smart-AI-Recipe-Genius
Smart AI Recipe Genius is an AI-powered web app that detects vegetables from images and generates cuisine-based recipes using LLMs. It also provides health insights, shopping lists, and food waste reduction tips through a clean, user-friendly interface.

---

## 🌟 Key Highlights

- 📷 Upload an image of vegetables
- 🥦 Automatic vegetable detection using **YOLO**
- 🌍 Choose from fixed cuisines:
  - Indian
  - French
  - Mexican
  - Thai
  - Korean
- 🍽️ Get a curated list of dishes per cuisine
- 🔄 Refresh to explore new dish suggestions
- 🤖 AI-generated recipe instructions using **Groq (LLaMA models)**
- 🛒 Auto-generated shopping list
- ❤️ Health report (calories, health score, level)
- ♻️ Food waste reduction tips
- 🌿 Full-screen greenery-themed UI built with **Streamlit**

---

## 🧠 How It Works (Pipeline)

1. **Image Upload**  
   User uploads an image containing vegetables.

2. **Vegetable Detection (YOLO)**  
   The system detects vegetables from the image using a YOLO-based object detection model.

3. **Cuisine & Dish Selection**  
   User selects a cuisine and chooses a dish from a fixed, curated list.

4. **AI Recipe Generation (Groq)**  
   The selected dish and detected vegetables are sent to Groq’s LLaMA model to generate:
   - Recipe description
   - Ingredients
   - Step-by-step cooking instructions

5. **Additional Intelligence**
   - Shopping list extraction
   - Health score and calorie estimation
   - Food waste reduction suggestions

---

## 🛠️ Tech Stack

- **Frontend & UI**
  - Streamlit
  - Custom CSS (greenery & glassmorphism theme)

- **Backend & AI**
  - Python
  - Groq API (LLaMA models)
  - Prompt-based recipe generation

- **Computer Vision**
  - YOLO (Ultralytics)
  - OpenCV

- **Utilities**
  - NumPy
  - Pillow
  - Requests

---

## 📁 Project Structure

```text
smart_recipe_generator/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── ai/
│   ├── llm_api.py
│   ├── recipe_creator.py
│   ├── health_calc.py
│   ├── waste_planner.py
│   └── __init__.py
│
├── helpers/
│   ├── img_tools.py
│   ├── qty_estimator.py
│   ├── cuisine_data.py
│   └── __init__.py
│
└── yolo/
    └── detect.py

---

## ▶️ How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/smart-ai-recipe-genius.git
cd smart-ai-recipe-genius

python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt

.streamlit/secrets.toml

GROQ_API_KEY = "your_groq_api_key_here"

streamlit run app.py



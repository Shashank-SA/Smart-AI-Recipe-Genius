import streamlit as st

from helpers.img_tools import save_uploaded_image, resize_image, validate_image
from yolo.detect import detect_vegetables
from ai.recipe_creator import create_recipe, create_shopping_list
from helpers.qty_estimator import estimate_quantities
from ai.waste_planner import generate_waste_reduction_tips
from ai.health_calc import calculate_health_report
from ai.llm_api import generate_recipe_names
from helpers.cuisine_data import CUISINE_DISHES


# ======================================================
# 🌿 FULL-SCREEN GREENERY THEME
# ======================================================
def apply_greenery_theme():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(
                rgba(0, 80, 40, 0.88),
                rgba(0, 0, 0, 0.95)
            ),
            url("https://images.unsplash.com/photo-1506806732259-39c2d0268443");
            background-size: cover;
            background-attachment: fixed;
        }

        section[data-testid="stMain"] {
            padding: 2rem 4rem;
        }

        .glass {
            background: rgba(0, 0, 0, 0.6);
            backdrop-filter: blur(12px);
            border-radius: 18px;
            padding: 26px;
            margin-bottom: 30px;
        }

        h1, h2, h3 {
            color: #baffc9;
        }

        .stButton>button {
            background-color: #2ecc71;
            color: black;
            font-weight: bold;
            border-radius: 14px;
        }

        .stSelectbox>div>div {
            background-color: #203020;
        }

        .stSlider > div {
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


apply_greenery_theme()


# ======================================================
# 🧠 PAGE HEADER
# ======================================================
st.title("🧑‍🍳 Smart AI Recipe Genius")
st.markdown(
    "### 🥗 *Cook smarter, eat healthier, waste less.*"
)
st.caption(
    "Upload vegetables → Get AI-powered recipes, health insights & food waste reduction tips"
)

st.markdown("<hr>", unsafe_allow_html=True)


# ======================================================
# 📤 IMAGE UPLOAD
# ======================================================
st.markdown('<div class="glass">', unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "📷 Upload an image of vegetables",
    type=["jpg", "jpeg", "png"]
)

st.markdown('</div>', unsafe_allow_html=True)


# ======================================================
# 🖼️ IMAGE PROCESSING + DETECTION
# ======================================================
if uploaded_file:
    image_path = save_uploaded_image(uploaded_file)

    if not validate_image(image_path):
        st.error("Invalid image format")
        st.stop()

    resized_image = resize_image(image_path)
    st.image(resized_image, width=800)

    vegetables = detect_vegetables(image_path)

    if not vegetables:
        st.warning("No vegetables detected.")
        st.stop()

    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.success("🥦 Vegetables detected:")
    for veg in vegetables:
        st.write(f"- {veg}")
    st.markdown('</div>', unsafe_allow_html=True)


    # ======================================================
    # 🌍 CUISINE SELECTION (FIXED + REFRESH)
    # ======================================================
    st.markdown('<div class="glass">', unsafe_allow_html=True)

    cuisine = st.selectbox(
        "🌎 Choose Cuisine Type",
        list(CUISINE_DISHES.keys())
    )

    if "dish_index" not in st.session_state:
        st.session_state.dish_index = 0

    if st.button("🔄 Refresh Dishes"):
        st.session_state.dish_index += 10

    dishes = CUISINE_DISHES[cuisine]
    start = st.session_state.dish_index % len(dishes)
    end = start + 10

    visible_dishes = dishes[start:end]

    selected_recipe = st.selectbox(
        "🍽️ Select a Dish",
        visible_dishes
    )

    servings = st.slider(
        "👨‍👩‍👧 Number of servings",
        min_value=1,
        max_value=10,
        value=2
    )

    st.markdown('</div>', unsafe_allow_html=True)


    # ======================================================
    # 🍳 RECIPE GENERATION
    # ======================================================
    if st.button("🍳 Generate Recipe"):
        st.markdown('<div class="glass">', unsafe_allow_html=True)

        recipe_text = create_recipe(selected_recipe, vegetables)
        st.markdown("## 📖 Recipe")
        st.markdown(recipe_text)

        st.markdown('</div>', unsafe_allow_html=True)


        # ======================================================
        # 🛒 SHOPPING LIST
        # ======================================================
        st.markdown('<div class="glass">', unsafe_allow_html=True)

        shopping_list = create_shopping_list(recipe_text)
        quantities = estimate_quantities(shopping_list, servings)

        st.markdown("## 🛍️ Shopping List")
        for item in quantities:
            st.write(f"- {item}")

        st.markdown('</div>', unsafe_allow_html=True)


        # ======================================================
        # ❤️ HEALTH REPORT
        # ======================================================
        st.markdown('<div class="glass">', unsafe_allow_html=True)

        health = calculate_health_report(vegetables)
        st.markdown("## ❤️ Health Report")
        st.write(f"Calories: {health.get('calories', 'N/A')}")
        st.write(f"Health Score: {health.get('score', 'N/A')}")
        st.write(f"Level: {health.get('level', 'N/A')}")


        st.markdown('</div>', unsafe_allow_html=True)


        # ======================================================
        # ♻️ WASTE REDUCTION
        # ======================================================
        st.markdown('<div class="glass">', unsafe_allow_html=True)

        tips = generate_waste_reduction_tips(vegetables)
        st.markdown("## ♻️ Food Waste Reduction Tips")
        for tip in tips:
            st.write(f"- {tip}")

        st.markdown('</div>', unsafe_allow_html=True)

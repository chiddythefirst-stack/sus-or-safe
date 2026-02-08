import streamlit as st
from PIL import Image
import os

# -------------------------
# Helper function
# -------------------------
def load_image_safe(file_name):
    """
    Load image safely. Returns PIL image if exists, else None.
    """
    path = os.path.join("assets", file_name)
    if os.path.exists(path):
        try:
            return Image.open(path)
        except:
            st.warning(f"⚠️ Could not open image: {file_name}")
            return None
    else:
        st.warning(f"⚠️ Image not found: {file_name}")
        return None

# -------------------------
# App setup
# -------------------------
st.set_page_config(page_title="Sus or Safe", layout="centered")

# Load logo safely
logo = load_image_safe("logo.png")
if logo:
    st.image(logo, width=120)

st.title("🛡️ Sus or Safe: Internet Safety Game")

# -------------------------
# Level selection
# -------------------------
level = st.radio("Choose your level:", ["EYFS", "Primary"])

# -------------------------
# Scenarios
# -------------------------
eyfs_scenarios = [
    {"text": "You see a cartoon video from your teacher.", "image": "eyfs_scenario1.png", "answer": "green"},
    {"text": "A friend sends you a sticker in a game.", "image": "eyfs_scenario2.png", "answer": "green"},
    {"text": "Someone you don’t know asks your name.", "image": "eyfs_scenario3.png", "answer": "red"},
    {"text": "A cartoon asks you to share your house address.", "image": "eyfs_scenario4.png", "answer": "red"},
    {"text": "You get a safe coloring game on the tablet.", "image": "eyfs_scenario5.png", "answer": "green"},
    {"text": "A stranger asks you to follow them.", "image": "eyfs_scenario6.png", "answer": "red"},
    {"text": "You watch a fun animal video from your class.", "image": "eyfs_scenario7.png", "answer": "green"},
    {"text": "Someone sends a scary picture.", "image": "eyfs_scenario8.png", "answer": "red"},
]

primary_scenarios = [
    {"text": "You receive a link from a friend to play a new online game.", "image": "primary_scenario1.png", "answer": "green"},
    {"text": "An unknown person messages you asking for your password.", "image": "primary_scenario2.png", "answer": "red"},
    {"text": "Your friend asks you to share a funny meme.", "image": "primary_scenario3.png", "answer": "green"},
    {"text": "Someone you don’t know asks to video call you.", "image": "primary_scenario4.png", "answer": "red"},
    {"text": "A website asks for your school login to access homework.", "image": "primary_scenario5.png", "answer": "green"},
    {"text": "A pop-up asks you to download a random file.", "image": "primary_scenario6.png", "answer": "red"},
    {"text": "A friend shares a link to an online quiz about school.", "image": "primary_scenario7.png", "answer": "green"},
    {"text": "A stranger says you’ll win money if you click a link.", "image": "primary_scenario8.png", "answer": "red"},
    {"text": "Your teacher sends you instructions for a school project.", "image": "primary_scenario9.png", "answer": "green"},
    {"text": "Someone in a chat group posts personal info about you.", "image": "primary_scenario10.png", "answer": "red"},
]

# -------------------------
# Pick scenarios based on level
# -------------------------
scenarios = eyfs_scenarios if level == "EYFS" else primary_scenarios

# -------------------------
# Session state for score and index
# -------------------------
if "score" not in st.session_state:
    st.session_state.score = 0
if "index" not in st.session_state:
    st.session_state.index = 0

# -------------------------
# Show scenario
# -------------------------
if st.session_state.index < len(scenarios):
    scenario = scenarios[st.session_state.index]
    
    # EYFS colorful background
    if level == "EYFS":
        st.markdown(
            """
            <style>
            .stApp {
                background-color: #FFF1B5;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    
    # Show scenario image safely
    scenario_img = load_image_safe(scenario["image"])
    if scenario_img:
        st.image(scenario_img, width=300)
    
    st.write(f"**Scenario:** {scenario['text']}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🟢 Safe"):
            if scenario["answer"] == "green":
                st.success("✅ Correct!")
                st.session_state.score += 1
            else:
                st.error("❌ Oops! That was unsafe!")
            st.session_state.index += 1
            st.experimental_rerun()
            
    with col2:
        if st.button("🔴 Sus"):
            if scenario["answer"] == "red":
                st.success("✅ Correct!")
                st.session_state.score += 1
            else:
                st.error("❌ Oops! That was safe!")
            st.session_state.index += 1
            st.experimental_rerun()
else:
    st.balloons()
    st.markdown(f"### 🎉 Well done! You scored {st.session_state.score} out of {len(scenarios)}")
    st.write("Remember: Always think before sharing personal info online. Stay safe and smart! 🌐🛡️")

# -------------------------
# Reset button
# -------------------------
if st.button("🔄 Reset Game"):
    st.session_state.score = 0
    st.session_state.index = 0
    st.experimental_rerun()
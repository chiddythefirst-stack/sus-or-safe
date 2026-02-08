import streamlit as st
from PIL import Image
import os

# -------------------------
# Safe logo loader (logo in same folder as script)
# -------------------------
def load_logo(file_name="logo.png"):
    # Absolute path to the current script folder
    base_path = os.path.dirname(os.path.abspath(__file__))
    logo_path = os.path.join(base_path, file_name)

    if os.path.exists(logo_path):
        try:
            return Image.open(logo_path)
        except:
            st.warning("⚠️ Could not open the logo file.")
            return None
    else:
        st.info("Logo not found, continuing without logo.")
        return None

# -------------------------
# App setup
# -------------------------
st.set_page_config(page_title="Sus or Safe", layout="centered")

# Load and show logo
logo = load_logo()
if logo:
    st.image(logo, width=120)

st.title("🛡️ Sus or Safe: Internet Safety Game")

# -------------------------
# Level selection
# -------------------------
level = st.radio("Choose your level:", ["EYFS", "Primary"])

# -------------------------
# Scenarios (no images)
# -------------------------
eyfs_scenarios = [
    {"text": "You see a cartoon video from your teacher.", "answer": "green"},
    {"text": "A friend sends you a sticker in a game.", "answer": "green"},
    {"text": "Someone you don’t know asks your name.", "answer": "red"},
    {"text": "A cartoon asks you to share your house address.", "answer": "red"},
    {"text": "You get a safe coloring game on the tablet.", "answer": "green"},
    {"text": "A stranger asks you to follow them.", "answer": "red"},
    {"text": "You watch a fun animal video from your class.", "answer": "green"},
    {"text": "Someone sends a scary picture.", "answer": "red"},
]

primary_scenarios = [
    {"text": "You receive a link from a friend to play a new online game.", "answer": "green"},
    {"text": "An unknown person messages you asking for your password.", "answer": "red"},
    {"text": "Your friend asks you to share a funny meme.", "answer": "green"},
    {"text": "Someone you don’t know asks to video call you.", "answer": "red"},
    {"text": "A website asks for your school login to access homework.", "answer": "green"},
    {"text": "A pop-up asks you to download a random file.", "answer": "red"},
    {"text": "A friend shares a link to an online quiz about school.", "answer": "green"},
    {"text": "A stranger says you’ll win money if you click a link.", "answer": "red"},
    {"text": "Your teacher sends you instructions for a school project.", "answer": "green"},
    {"text": "Someone in a chat group posts personal info about you.", "answer": "red"},
]

# Pick scenarios based on level
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
import streamlit as st
import random

st.set_page_config(
    page_title="SUS or SAFE",
    page_icon="🛡️",
    layout="centered"
)

# ---------- STYLE ----------
st.markdown("""
<style>
.title {
    font-size:50px;
    text-align:center;
    color:#2E8B57;
    font-weight:bold;
}
.scenario {
    font-size:28px;
    text-align:center;
    padding:20px;
}
.score {
    font-size:22px;
    text-align:center;
    color:#444;
}
.end {
    font-size:36px;
    text-align:center;
    color:#FF9800;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# ---------- LOGO ----------
st.image("logo.png", width=120)

st.markdown('<div class="title">🛡️ SUS or SAFE 🛡️</div>', unsafe_allow_html=True)

# ---------- LEVEL ----------
level = st.radio("Choose Level 👇", ["EYFS", "Primary"], horizontal=True)

# ---------- QUESTIONS ----------
EYFS = [
    ("Using the iPad with an adult 👩‍👧", "SAFE", "images/adult.png"),
    ("A stranger says Hi 👋", "SUS", "images/stranger.png"),
    ("Watching YouTube Kids 🎥", "SAFE", "images/youtube.png"),
    ("Clicking a pop-up game 🎮", "SUS", "images/popup.png"),
    ("Telling teacher when scared 🧑‍🏫", "SAFE", "images/teacher.png"),
]

PRIMARY = [
    ("Someone asks for your name online 👤", "SUS", None),
    ("Keeping your password secret 🔐", "SAFE", None),
    ("YOU WON! Click here 🎁", "SUS", None),
    ("Blocking someone mean 🚫", "SAFE", None),
    ("Downloading a game without asking ❌", "SUS", None),
]

questions = EYFS if level == "EYFS" else PRIMARY
TOTAL = len(questions)

# ---------- SESSION STATE ----------
if "index" not in st.session_state:
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.feedback = ""
    st.session_state.order = random.sample(questions, TOTAL)

# ---------- RESET BUTTON ----------
if st.button("🔄 Reset Game"):
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.feedback = ""
    st.session_state.order = random.sample(questions, TOTAL)
    st.experimental_rerun()

# ---------- END SCREEN ----------
if st.session_state.index >= TOTAL:
    st.markdown('<div class="end">🏆 INTERNET SAFETY HERO 🏆</div>', unsafe_allow_html=True)
    st.markdown(f"### ⭐ Final Score: {st.session_state.score} / {TOTAL}")
    st.balloons()
    st.stop()

# ---------- CURRENT QUESTION ----------
question, answer, image = st.session_state.order[st.session_state.index]

st.markdown(f'<div class="scenario">{question}</div>', unsafe_allow_html=True)

if level == "EYFS" and image:
    st.image(image, width=300)

# ---------- BUTTONS ----------
col1, col2 = st.columns(2)

with col1:
    if st.button("🟢 SAFE"):
        if answer == "SAFE":
            st.session_state.feedback = "🎉 SAFE! WELL DONE!"
            st.session_state.score += 1
            st.audio("sounds/correct.mp3")
        else:
            st.session_state.feedback = "🚨 OOPS! THAT WAS SUS!"
            st.audio("sounds/wrong.mp3")
        st.session_state.index += 1
        st.experimental_rerun()

with col2:
    if st.button("🔴 SUS"):
        if answer == "SUS":
            st.session_state.feedback = "🎉 CORRECT! THAT IS SUS!"
            st.session_state.score += 1
            st.audio("sounds/correct.mp3")
        else:
            st.session_state.feedback = "🚨 OOPS! THAT WAS SAFE!"
            st.audio("sounds/wrong.mp3")
        st.session_state.index += 1
        st.experimental_rerun()

# ---------- SCORE ----------
st.markdown(f'<div class="score">⭐ Score: {st.session_state.score}</div>', unsafe_allow_html=True)
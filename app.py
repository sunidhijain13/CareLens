import streamlit as st
from chatbot import ask_gpt
from emotion_detector import detect_emotion

# Set page config
st.set_page_config(page_title="CareLens", page_icon="🌼", layout="centered")

# 🌸 Custom CSS for pastel UI
st.markdown(
    """
    <style>
    body {
        background-color: #fffafc;
    }
    .stApp {
        background: linear-gradient(to bottom, #fff0f5 0%, #ffffff 100%);
        padding: 3rem 1rem;
        font-family: 'Segoe UI', sans-serif;
    }
    .stTextArea textarea {
        background-color: #fff5f8;
        border: 1px solid #ffc0cb;
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #ffb6c1;
        color: white;
        border-radius: 10px;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🌼 Centered logo
#col1, col2, col3 = st.columns([1, 3, 1])
#with col2:
#    st.image("assets/CareLens.png", width=120)
#I was using this code earlier but the image was not being centered so tried something more advanced below
from PIL import Image
import base64


def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


image_base64 = get_base64_image("assets/CareLens.png")
st.markdown(
    f"""
    <div style='text-align: center;'>
        <img src='data:image/png;base64,{image_base64}' width='120'/>
    </div>
    """,
    unsafe_allow_html=True
)


# 📝 Custom headers with hierarchy
st.markdown("""
    <div style="text-align: center;">
        <h1 style="color: #e91e63; font-size: 36px; margin-bottom: 0;">🌼 CareLens</h1>
        <p style="font-size: 20px; font-weight: bold; color: #444;">Your Emotional Wellness Companion</p>
        <p style="font-size: 16px; color: #666;">Hi there! I'm here to check in with you. How are you feeling today?</p>
    </div>
""", unsafe_allow_html=True)

# ✍️ Input area
user_input = st.text_area(
    "",
    placeholder="Write your thoughts, how your day went, or anything on your mind...",
    height=160
)

# 💬 Reflect Button
submit_col1, submit_col2, submit_col3 = st.columns([1, 2, 1])
with submit_col2:
    if st.button("💬 Reflect with CareLens", use_container_width=True):
        if user_input.strip():
            with st.spinner("Thinking with heart..."):
                emotion, score = detect_emotion(user_input)
                gpt_reply = ask_gpt(user_input)

            # Emotion Output
            st.subheader("🧠 Detected Emotion")
            st.success(f"{emotion} ({score * 100:.1f}%)")

            # GPT Response
            st.subheader("💬 CareLens says:")
            st.write(gpt_reply)
        else:
            st.warning("Please write something first 🌷")

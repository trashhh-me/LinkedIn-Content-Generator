# app.py
from gemini_engine import generate_post
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# --- Load .env & Configure Gemini ---
load_dotenv()
api_key = os.getenv("Gemini_API_Key")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")


# --- Page Config ---
st.set_page_config(page_title="LinkedIn Post Generator", layout="centered")

st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
        font-family: 'Arial', sans-serif;  
        color: white;  
    }

    textarea,input{
        font-family: 'Arial', sans-serif;  
        color = white !important;
    }
    [data-testid="stMarkdownContainer"] > label,
    label {
        color: white !important;
    }
    div[role="radiogroup"] label span {
    color: white !important;
    }
    .stSelectbox div[role="button"] {
        color: black !important;
    }
ß
    </style>
    """,
    unsafe_allow_html=True
)

# --- Title ---
st.title("🤖 LinkedIn Content Generator Bot")

st.markdown("""
Welcome! Let's create a high-performing LinkedIn post.
Fill out the details below and let the bot work its magic! ✨
""")

# --- Input Fields ---
topic = st.text_area("📝 What's your post about?", placeholder="e.g., My journey learning AI, launching a new product...")

tone = st.selectbox(
    "🎭 Choose a tone for the post:",
    ["Professional", "Inspirational", "Humorous", "Opinionated", "Casual", "Storytelling"]
)

audience = st.text_input("👥 Who's your target audience? (Optional)", placeholder="e.g., Recruiters, Tech leads, Founders")

length = st.radio(
    "📏 Preferred post length:",
    ["Short (under 500 chars)", "Medium (500–1500)", "Long (1500–3000)"]
)

hashtags = st.text_input("🏷️ Hashtags (Optional, comma-separated)", placeholder="#AI, #career, #growth")

# --- Submit Button ---
submit = st.button("🚀 Generate My Post")

# --- Trigger (Mock Output for Now) ---
if submit:
    if not topic.strip():
        st.warning("Please enter what your post is about.")
    else:
        prompt = f"""
        Write a {length.lower()} LinkedIn post in a {tone.lower()} tone about:
        "{topic.strip()}".

        Audience: {audience or "General LinkedIn"}.
        Include these hashtags at the end: {hashtags or "None"}.
        Start with a hook, keep it authentic and human. Format it nicely.
        """

        with st.spinner("Generating your epic LinkedIn post... 💡"):
            output = generate_post(prompt)

        st.success("✅ Post generated!")
        st.markdown("### 📝 Here's your LinkedIn Post:")
        st.text_area("Generated Post", value=output, height=300)

        # --- Copy to Clipboard ---
        st.code(output, language='markdown')
        st.download_button("📋 Copy Post", output, file_name="linkedin_post.txt")

        # --- Regenerate Button ---
        if st.button("🔁 Regenerate"):
            st.experimental_rerun()
import streamlit as st
from panini_test import yan_sandhi, guna_sandhi
from gtts import gTTS
from io import BytesIO

# 1. Custom CSS for Vedic Theme
st.markdown("""
    <style>
    .main {
        background-color: #fff5e6;
    }
    .title-text {
        color: #ff4500;
        text-align: center;
        font-family: 'Arial';
        border-bottom: 2px solid #ff4500;
        padding-bottom: 10px;
    }
    .stButton>button {
        background-color: #ff4500;
        color: white;
        width: 100%;
        border-radius: 5px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Header
st.markdown("<h1 class='title-text'>🕉️ Panini AI Engine v2.0</h1>", unsafe_allow_html=True)
st.write("---")
st.subheader("Sanskrit Sandhi Automator by Vikram")

# 3. User Inputs
col1, col2 = st.columns(2)
with col1:
    word1 = st.text_input("Pehla Shabd (e.g., महा)", "महा")
with col2:
    word2 = st.text_input("Doosra Shabd (e.g., इंद्र)", "इंद्र")

# 4. Action Button and Logic
if st.button("Sutra Apply Karo"):
    # Pehle check karo Guna Sandhi
    result = guna_sandhi(word1, word2)
    
    # Agar Guna nahi hai toh Yan check karo
    if not result:
        result = yan_sandhi(word1, word2)
    
    # Agar result mil gaya
    if result:
        st.success(f"### Result: {result}")
        
        # --- Voice/Audio Upgrade ---
        try:
            tts = gTTS(text=result, lang='hi')
            fp = BytesIO()
            tts.write_to_fp(fp)
            st.audio(fp)
            st.info("🔊 Upar click karke pronunciation suniye!")
        except Exception as e:
            st.warning("Audio generate nahi ho paya, par result sahi hai!")
            
    else:
        st.error("Abhi is rule par research chal rahi hai! (v2.0)")

st.write("---")
st.caption("Developed with ❤️ for Sanskrit Grammar")
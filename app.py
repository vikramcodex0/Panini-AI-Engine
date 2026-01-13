import streamlit as st

# 1. Custom CSS (Kyunki tumhe HTML/CSS pasand hai!)
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
st.markdown("<h1 class='title-text'>🕉️ Panini AI Engine v1.0</h1>", unsafe_allow_html=True)
st.write("---")
st.subheader("Sanskrit Sandhi Automator by Vikram")

# 3. User Inputs
col1, col2 = st.columns(2)
with col1:
    word1 = st.text_input("Pehla Shabd (e.g., iti)", "iti")
with col2:
    word2 = st.text_input("Doosra Shabd (e.g., adi)", "adi")

# 4. Asli Panini Logic (Jo tune terminal mein test kiya tha)
def smart_sandhi(w1, w2):
    last = w1[-1].lower()
    first = w2[0].lower()
    
    # Rule 3: Yan Sandhi (Jo tune subah add kiya!)
    if last == "i" and first != "i":
        res = w1[:-1] + "y" + w2
        st.success(f"**Result:** {res}")
        st.info("📜 **Sutra:** Iko Yanachi (6.1.77) apply hua.")
    
    # Rule 1: Guna Sandhi
    elif last == "a" and first == "i":
        res = w1[:-1] + "e" + w2[1:]
        st.success(f"**Result:** {res}")
        st.info("📜 **Sutra:** Ad Guna (6.1.87) apply hua.")
        
    else:
        st.warning("Result: " + w1 + w2 + " (Abhi is rule par research chal rahi hai!)")

# 5. Action Button
if st.button("Sutra Apply Karo"):
    smart_sandhi(word1, word2)
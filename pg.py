import streamlit as st

def generate_password(length):
    chars = "abcABC123!@#"
    return ''.join(chars[i % len(chars)] for i in range(length))

st.title("🔐 Password Generator")

length = st.slider("Length", 20, 8)

if st.button("Generate"):
    st.success(generate_password(length))

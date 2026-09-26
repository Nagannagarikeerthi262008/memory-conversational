import streamlit as st
st.title("Welcome To AI ChatBOT")
P = st.text_input("KEERTHI REDDY")
R = st.button("Enter")
if R:
    if P:
        st.success("SUCCESS")
    else:
        st.error("ERROR")


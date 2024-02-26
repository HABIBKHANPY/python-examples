import streamlit as st
import random
menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
if choice == "Home":
        st.subheader("Home")

import streamlit as st
import random

# Get user's name
name = st.text_input("Enter your name:")

# Sidebar menu
st.sidebar.title("Menu")
selected_page = st.sidebar.radio("", ["Address Book", "About Us", "Contact"])

if selected_page == "Address Book":
    st.title("Address Book")
    # Add address book functionality here
elif selected_page == "About Us":
    st.title("About Us")
    st.write(f"This address book application was created by {name}.")
elif selected_page == "Contact":
    st.title("Contact")
    st.write("For support, please email support@example.com.")

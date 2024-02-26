import streamlit as st
import random

# Define main function
def main():
    st.balloons()
    st.snow()

    # Sidebar menu
    st.sidebar.title("Menu")
    selected_page = st.sidebar.radio("", ["MAGIC 8 BALL GAME", "About Us", "Contact"])

    if selected_page == "MAGIC 8 BALL GAME":
        magic_8_ball_game()
    elif selected_page == "About Us":
        about_us()
    elif selected_page == "Contact":
        contact()

# Define Magic 8 Ball game function
def magic_8_ball_game():
    st.title("BANO QABIL 2.0 PROJECT")
    st.title("MAGIC 8 BALL")

    # Magic 8 Ball answers
    responses = [
         "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes - definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]

    question = st.text_input("Ask a question:")
    if st.button("Shake the Magic 8 Ball"):
        answer = random.choice(responses)
        st.markdown(f"<h2 style='text-align: center;'>🔮 {answer}</h2>", unsafe_allow_html=True)

# Define About Us function
def about_us():
    st.title("About Us")
    name = "Bano Qabli 2.0 CIT+Python "  # Define the name or modify as needed
    st.write(f"This address book application was created by {name}.")

# Define Contact function
def contact():
    st.title("Contact")
    st.write("For support, please email support@example.com.")

# Custom CSS
def load_custom_css():
    st.markdown("""
        <style>
        /* Your CSS styles */
        </style>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    load_custom_css()
    main()

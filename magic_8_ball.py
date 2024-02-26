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
       M
import streamlit as st
import random
st.balloons()
st.snow()

# Sidebar menu
st.sidebar.title("Menu")
selected_page = st.sidebar.radio("", ["MAGIC 8 BALL GAME", "About Us", "Contact"])

if selected_page == "MAGIC 8 BALL GAME":
    st.title("BANO QABIL 2.0 PROJECT")
    st.title("MAGIC 8 BALL")
        # Add address book functionality here
elif selected_page == "About Us":
    st.title("About Us")
    st.write(f"This address book application was created by {name}.")
elif selected_page == "Contact":
    st.title("Contact")
    st.write("For support, please email support@example.com.")
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

def main():
    # Custom CSS to inject into the webpage
    st.markdown("""
        <style>
        .stApp {
            background-image: url('https://img.hotimg.com/eight-ball.jpeg');
            background-size: cover;
            color: #ffffff;
        }
        .stTextInput>div>div>input {
    color: #e0e0e0;
    background-color: #333333;
    }
    ]

    question = st.text_input("Ask a question:")
    if st.button("Shake the Magic 8 Ball"):
        answer = random.choice(responses)
        st.markdown(f"<h2 style='text-align: center;'>🔮 {answer}</h2>", unsafe_allow_html=True)

# Define About Us function
def about_us():
    st.title("About Us")
    name = "Your Name or Company Name"  # Define the name or modify as needed
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

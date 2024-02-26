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
    elif selected_page == "ABOUT US":
        about_us()
    elif selected_page == "CONTACT":
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
    name = "MUHAMMAD HABIB KHAN PROJECT GROUP LEADER AND GROUP MEMBER HAMMAD RAZA & MUZAFFAR KHAN"
    st.write("magic 8 ball final project bano qbil 2.0 This section of the web application is an interactive Magic 8 Ball game. The user can ask a question, and the Magic 8 Ball provides a random response from a predefined list. It's a fun and engaging way to simulate the classic toy. The game is designed with user-friendly elements and appealing visuals, enhancing the interactivity and enjoyment of the experience.")
    st.write(f"This application was created by {name}.")


# Define Contact function
def contact():
    st.title("Contact")
    st.write("For support, questions, or feedback, please reach out to us.")
    st.write("📧 Email: hk898243@gmail.com")
    st.write("📞 Contact Number: 03131016682")

# Custom CSS
def load_custom_css():
    st.markdown("""
        <style>
        /* Your CSS styles */
        .stApp {
            background-image: url('https://img.hotimg.com/eight-ball.jpeg');
            background-size: cover;
            color: #ffffff;
        }
        </style>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    load_custom_css()
    main()

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
    name = "Bano Qabli 2.0 CIT+Python"  # Define the name or modify as needed
    st.write(f"This address book application was created by {name}.")
    st.write("""Magic 8 Ball Game BANO QABIL 2.0 PROJECT
This section of the web application is an interactive Magic 8 Ball game. The user can ask a question, and the Magic 8 Ball provides a random response from a predefined list. It's a fun and engaging way to simulate the classic toy. The game is designed with user-friendly elements and appealing visuals, enhancing the interactivity and enjoyment of the experience.

About Us
The "About Us" page provides information about the creators and the purpose behind the project. Here you can include details about yourself or your team, the motivation for creating this application, and any other relevant information that adds a personal touch to the project. This section helps to establish a connection with the users and gives them insight into the people behind the application.

Contact
In the "Contact" section, users can find information on how to reach out for support or inquiries. This could include an email address, social media links, or a contact form. Providing clear and accessible contact information is crucial for maintaining engagement with your user base and offering them the necessary support.

Description of the Project
Project Name: BANO QABIL 2.0 PROJECT

Description:
The BANO QABIL 2.0 PROJECT is an innovative web application developed using Streamlit, aimed at providing a delightful and interactive user experience. At the heart of this application is the "Magic 8 Ball Game", which brings a digital twist to the nostalgic toy, offering users mystical answers to their pressing questions.

The application is built with a focus on simplicity and user engagement. The intuitive design ensures that users of all ages can easily navigate and enjoy the game. The "About Us" section offers a glimpse into the creative minds behind the project, highlighting their dedication and passion. Meanwhile, the "Contact" page ensures open channels of communication, fostering a community around the application.

This project is not just a game; it's a testament to the power of creative coding and user-centered design. It represents a bridge between playful curiosity and technological innovation, inviting users to enjoy a moment of fun in their daily lives.""")

# Define Contact function
def contact():
    st.title("Contact")
    st.write("For support, please email support@example.com.")

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

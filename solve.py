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
    st.title("BANO QABIL 2.0 FINAL PROJECT")
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
    st.markdown("""
        Bano Qabil 2.0 Final project is a project led by Muhammad Habib Khan and includes group members Hammad Raza and Muzaffar Khan. 
        The purpose of this project is to showcase the magic of the digital world through interactive applications. 
        Feel free to explore and enjoy the Magic 8 Ball game and other features of Bano Qabil 2.0.
        Main Function (main):

This function serves as the entry point of the Streamlit application. It starts with displaying balloons and snow animations on the app using st.balloons() and st.snow().
A sidebar menu is created using st.sidebar.title("Menu") and st.sidebar.radio(...), allowing users to choose between different pages: "MAGIC 8 BALL GAME", "About Us", and "Contact".
Magic 8 Ball Game (magic_8_ball_game):

This function renders a page titled "BANO QABIL 2.0 PROJECT" and "MAGIC 8 BALL".
Users can input a question in a text box, and upon clicking the "Shake the Magic 8 Ball" button, a random response from a predefined list (responses) is displayed. This mimics the functionality of a traditional Magic 8 Ball toy.
About Us Page (about_us):

This page displays information about the creators of the project ("MUHAMMAD HABIB KHAN PROJECT GROUP LEADER AND GROUP MEMBER HAMMAD RAZA & MUZAFFAR KHAN") and gives a brief description of the project's purpose.
Contact Page (contact):

This section provides contact details like an email address and a phone number for support, questions, or feedback.
Custom CSS Styling (load_custom_css):

Applies custom CSS to the Streamlit app for styling purposes. The style includes a background image and text color changes.
Script Execution:

At the end of the script, if __name__ == "__main__": ensures that the load_custom_css() and main() functions are called when the script is run directly (not when imported as a module in another script). This is the standard way to run a Python script.
The script is a good example of how Python and Streamlit can be used to create interactive web applications with ease. The focus seems to be on providing a fun, interactive experience with the Magic 8 Ball game, along with informative pages about the project and its creators. The addition of custom CSS enhances the visual appeal of the application.
    """)

# Define Contact function
def contact():
    st.title("Contact")
    st.write("For support, questions, or feedback, please reach out to us.")
    st.write("📞 Contact Number: 03131016682")
    st.write("📧 Email: hk898243@gmail.com")
    
# Custom CSS
def load_custom_css():
    st.markdown("""
        <style>
            .stApp {
                background-image: url('https://img.hotimg.com/eight-ball.jpeg');
                background-size: cover;
                color: #ffffff;
                padding: 20px;  /* Add padding for better appearance */
            }
        </style>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    load_custom_css()
    main()

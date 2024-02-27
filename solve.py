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
        # ... (other responses)
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
        Bano Qabil 2.0 is a project led by Muhammad Habib Khan and includes group members Hammad Raza and Muzaffar Khan. 
        The purpose of this project is to showcase the magic of the digital world through interactive applications. 
        Feel free to explore and enjoy the Magic 8 Ball game and other features of Bano Qabil 2.0.
    """)

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

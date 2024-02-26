import streamlit as st
import random

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
            color: #4F4F4F;
        }
        .stButton>button {
    color: #1E90FF; /* Change text color to DodgerBlue */
    border-radius: 10px; /* Make corners less rounded */
    border-color: #32CD32; /* Change border color to LimeGreen */
    background-color: #FFD700; /* Change background color to Gold */
    font-size: 16px; /* Increase font size */
    padding: 10px 20px; /* Add more padding for a larger button */
    border-width: 2px; /* Make the border thicker */
    border-style: solid; /* Ensure the border is solid */
    box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.2); /* Add a subtle shadow */
    transition: background-color 0.3s, color 0.3s; /* Smooth transition for hover effect */
        }
        
.stButton>button:hover {
    background-color: #FF69B4; /* Change background color on hover to HotPink */
    color: #FFFFFF; /* Change text color on hover to white */
}
        </style>
        """, unsafe_allow_html=True)

    st.title("BANO QABIL PROJECT")
    st.title("MAGIC 8 BALL")

    # Text input for the question
    question = st.text_input("Ask a question:")

    if st.button("Shake the Magic 8 Ball"):
        answer = random.choice(responses)
        st.markdown(f"<h2 style='text-align: center;'>🔮 {answer}</h2>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()

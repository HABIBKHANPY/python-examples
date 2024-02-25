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
            background-image: url('https://your-background-image-url.jpg');
            background-size: cover;
            color: #ffffff;
        }
        .stTextInput>div>div>input {
            color: #4F4F4F;
        }
        .stButton>button {
            color: #4F4F4F;
            border-radius: 20px;
            border-color: #FF758C;
            background-color: #ffffff;
        }
        </style>
        """, unsafe_allow_html=True)

    st.title("Magic 8 Ball")

    # Text input for the question
    question = st.text_input("Ask a question:")

    if st.button("Shake the Magic 8 Ball"):
        answer = random.choice(responses)
        st.markdown(f"<h2 style='text-align: center;'>🔮 {answer}</h2>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()

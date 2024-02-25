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
    st.title("Magic 8 Ball")

    # Text input for the question
    question = st.text_input("Ask a question:")

    if st.button("Shake the Magic 8 Ball"):
        answer = random.choice(responses)
        st.write("🔮", answer)

if __name__ == "__main__":
    main()

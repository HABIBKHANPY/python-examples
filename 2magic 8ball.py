import streamlit as st
import random

# CSS to inject contained in a string
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

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
    local_css("style.css")  # Assuming you have a CSS file named 'style.css'

    st.title("Magic 8 Ball")

    # Create columns for better layout
    col1, col2, col3 = st.beta_columns([1,2,1])

    with col2:
        question = st.text_input("Ask a question:", key="question")

        if st.button("Shake the Magic 8 Ball"):
            answer = random.choice(responses)
            st.markdown(f"<h1 style='text-align: center; color: blue;'>🔮 {answer}</h1>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()

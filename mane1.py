import streamlit as st
import random

def magic_8_ball():
    st.title("Magic 8 Ball")
    
    # Add an image of a Magic 8 Ball for fun
    st.image("magic_8_ball.png", width=150)

    # Add a button to shake the Magic 8 Ball
    if st.button("Shake the Magic 8 Ball"):
        answer = get_random_answer()
        st.write(f"The Magic 8 Ball says: {answer}")

def get_random_answer():
    answers = [
        "Yes",
        "No",
        "Ask again later",
        "Cannot predict now",
        "Don't count on it",
        "Most likely",
        "Outlook not so good",
        "Reply hazy, try again"
    ]
    return random.choice(answers)

if __name__ == "__main__":
    magic_8_ball()

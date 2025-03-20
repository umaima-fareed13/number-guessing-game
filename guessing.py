import streamlit as st
import random

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background: linear-gradient(to right, #ff9a9e, #fad0c4);
            font-family: Arial, sans-serif;
        }
        .stButton>button {
            background-color: black;
            color: white;
            font-size: 18px;
            border-radius: 8px;
            padding: 10px 20px;
        }
        .stButton>button:hover {
            background-color: black;
        }
        .stNumberInput>div>div>input {
            font-size: 18px;
            padding: 5px;
        }
        .success {
            background-color: grey;
            color: white;
            padding: 10px;
            border-radius: 8px;
            text-align: center;
        }
        .error {
            background-color: grey;
            color: white;
            padding: 10px;
            border-radius: 8px;
            text-align: center;
        }
        .warning {
            background-color: grey;
            color: black;
            padding: 10px;
            border-radius: 8px;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'random_number' not in st.session_state:
    st.session_state.random_number = None
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'max_attempts' not in st.session_state:
    st.session_state.max_attempts = None
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# Title and description
st.markdown("<h1 style='text-align: center; color: grey;'>🎯 Number Guessing Game</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Try to guess the randomly generated number!</p>", unsafe_allow_html=True)

# Custom range selection
st.subheader("🎛 Choose a Number Range")
min_value = st.number_input("Minimum Value", value=1, step=1, min_value=1)
max_value = st.number_input("Maximum Value", value=100, step=1, min_value=min_value + 1)

# Difficulty selection
st.subheader("🎚 Select Difficulty Level")
difficulty = st.selectbox("Choose difficulty:", ["Easy (15)", "Medium (07 attempts)", "Hard (3 attempts)"])

# Set max attempts based on difficulty
if difficulty == "Easy (Unlimited)":
    st.session_state.max_attempts = None
elif difficulty == "Medium (10 attempts)":
    st.session_state.max_attempts = 10
elif difficulty == "Hard (5 attempts)":
    st.session_state.max_attempts = 5

# Start the game
if st.button("Start Game"):
    st.session_state.random_number = random.randint(min_value, max_value)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.success("✅ Game started! Enter your guess below.")

# User guess input
if st.session_state.random_number is not None and not st.session_state.game_over:
    guess = st.number_input("🎯 Enter your guess:", value=min_value, step=1, min_value=min_value, max_value=max_value)
    
    if st.button("Submit Guess"):
        st.session_state.attempts += 1

        if guess == st.session_state.random_number:
            st.markdown(f"<div class='success'>🎉 Congratulations! You guessed the number in {st.session_state.attempts} attempts.</div>", unsafe_allow_html=True)
            st.session_state.game_over = True
        elif guess < st.session_state.random_number:
            st.markdown("<div class='warning'>📉 Too low! Try again.</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='warning'>📈 Too high! Try again.</div>", unsafe_allow_html=True)

        # Check if max attempts reached
        if st.session_state.max_attempts is not None and st.session_state.attempts >= st.session_state.max_attempts:
            st.markdown(f"<div class='error'>❌ Game Over! The correct number was {st.session_state.random_number}.</div>", unsafe_allow_html=True)
            st.session_state.game_over = True

    st.write(f"🎯 **Attempts:** {st.session_state.attempts}")

# Reset button
if st.session_state.random_number is not None and st.button("🔄 Reset Game"):
    st.session_state.random_number = None
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.success("🔄 Game reset! Choose a new range and start again.")

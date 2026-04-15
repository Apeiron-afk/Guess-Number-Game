import streamlit as st
import random
import time

# Setting the page config
st.set_page_config(page_title="Guess A Number", page_icon="🤹")

# Initialize session state variables
if 'game_active' not in st.session_state:
    st.session_state.game_active = False
if 'random_number' not in st.session_state:
    st.session_state.random_number = None
if 'guess_attempt' not in st.session_state:
    st.session_state.guess_attempt = 1
if 'name' not in st.session_state:
    st.session_state.name = ""
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

st.title("🎭 Guess a Number Game 🎭")

# Name input section
if not st.session_state.name:
    st.session_state.name = st.text_input("Enter Your Name:", key="name_input")
    if st.session_state.name:
        st.rerun()

# Welcome message
if st.session_state.name and not st.session_state.game_active:
    st.write(f"Welcome user {st.session_state.name} 🤹")
    
    if st.button("Start New Game"):
        st.session_state.game_active = True
        st.session_state.game_over = False
        st.session_state.guess_attempt = 1
        st.session_state.random_number = random.randint(1, 13)
        
        with st.spinner("I am thinking of a number between 1 and 13 🧐. Please wait...."):
            time.sleep(1.5)
        
        st.success("Number is Generated ✅. Guess the Number in 4 attempts 🤹")
        st.rerun()

# Game logic
if st.session_state.game_active and not st.session_state.game_over:
    st.write(f"### Attempt {st.session_state.guess_attempt} of 4")
    
    guess = st.number_input(
        "Take a guess:",
        min_value=1,
        max_value=13,
        step=1,
        key="guess_input"
    )
    
    if st.button("Submit Guess"):
        if guess == st.session_state.random_number:
            st.balloons()
            st.success(f'🎉 Congratulation! Correct guess 🎉')
            st.success(f'You have guessed the number in {st.session_state.guess_attempt} attempt(s)')
            st.session_state.game_over = True
            st.session_state.game_active = False
        else:
            if guess > st.session_state.random_number:
                if st.session_state.guess_attempt < 4:
                    st.error('Your guess is TOO HIGH ⬆️. Think of a smaller number')
                else:
                    st.error('Your guess is TOO HIGH ⬆️')
            else:  # guess < random_number
                if st.session_state.guess_attempt < 4:
                    st.error('Your guess is TOO LOW ⬇️. Think of a bigger number')
                else:
                    st.error('Your guess is TOO LOW ⬇️')
            
            st.session_state.guess_attempt += 1
            
            if st.session_state.guess_attempt > 4:
                st.session_state.game_over = True
                st.session_state.game_active = False
                st.rerun()

# Game over message
if st.session_state.game_over:
    if st.session_state.guess_attempt > 4:
        st.error('☠️ Game Over! ☠️')
        st.error(f'The correct number was {st.session_state.random_number} 😓')
    
    if st.button("Play Again"):
        # Reset game state
        st.session_state.game_active = False
        st.session_state.game_over = False
        st.session_state.random_number = None
        st.session_state.guess_attempt = 1
        st.rerun()
    
    if st.button("Change Name"):
        st.session_state.name = ""
        st.session_state.game_active = False
        st.session_state.game_over = False
        st.rerun()
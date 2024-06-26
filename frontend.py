import streamlit as st
import requests

# URL of the Flask backend
backend_url = "https://909c-103-82-14-56.ngrok-free.app/roll"

st.title("Dice Roller")

if st.button("Roll Dice"):
    response = requests.get(backend_url)
    if response.status_code == 200:
        result = response.json().get("result")
        st.write(f"🎲 You rolled a {result}!")
    else:
        st.write("Error: Unable to get a response from the backend.")


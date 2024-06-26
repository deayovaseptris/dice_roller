import streamlit as st
import requests

# URL of the Flask backend
backend_url = "http://127.0.0.1:4040/roll"

st.title("Dice Roller")

if st.button("Roll Dice"):
    response = requests.get(backend_url)
    if response.status_code == 200:
        result = response.json().get("result")
        st.write(f"🎲 You rolled a {result}!")
    else:
        st.write("Error: Unable to get a response from the backend.")


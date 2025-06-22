import streamlit as st
import requests

st.title("📩 Spam Message Detector")

message = st.text_input("Enter a message:")

if st.button("Check"):
    if message.strip() == "":
        st.warning("Please enter a message.")
    else:
        response = requests.post(
            "http://localhost:5000/predict",
            json={"message": message}
        )
        if response.status_code == 200:
            result = response.json()["result"]
            if result == "spam":
                st.error("🚨 This is spam!")
            else:
                st.success("✅ This is ham (safe).")
        else:
            st.error("API Error. Check if Flask is running.")

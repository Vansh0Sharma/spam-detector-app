import streamlit as st
import joblib

# Load the trained model and vectorizer
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.title("📩 Spam Message Detector")

message = st.text_input("Enter a message:")

if st.button("Check"):
    if message.strip() == "":
        st.warning("Please enter a message.")
    else:
        vec = vectorizer.transform([message])
        prediction = model.predict(vec)[0]
        result = 'spam' if prediction == 1 else 'ham'
        if result == "spam":
            st.error("🚨 This is spam!")
        else:
            st.success("✅ This is ham (safe).")

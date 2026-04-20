import streamlit as st
import joblib

model = joblib.load("EmailClassifier.pkl")

st.title("IntelliSpam - Spam Email Classifier")
st.markdown("Enter an email message to check if it is spam or not.")

email = st.text_area("Enter email text:")

if st.button("Detect"):
    if email.strip() == "":
        st.warning("Please enter some text.")
    else:
        prediction = model.predict([email])[0]

        if prediction == 1:
            st.error("🚨 This is SPAM")
        else:
            st.success("✅ This is NOT Spam")

st.markdown("---")
st.markdown(
    "Made by **Arnav :)**  \n"
    "[GitHub](https://github.com/arnavmane) | "
    "[LinkedIn](https://linkedin.com/in/arnavmane21)"
)
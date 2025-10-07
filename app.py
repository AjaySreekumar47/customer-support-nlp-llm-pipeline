import streamlit as st
from src.pipeline import SupportPipeline

st.title("💬 Customer Support NLP Pipeline")
pipeline = SupportPipeline()

user_query = st.text_area("Enter customer query:", "My card hasn’t arrived yet, can I track delivery?")

if st.button("Generate Reply"):
    intent, summary, reply = pipeline.run(user_query)
    st.subheader("Predicted Intent")
    st.write(intent)
    st.subheader("Summary")
    st.write(summary)
    st.subheader("Reply")
    st.write(reply)

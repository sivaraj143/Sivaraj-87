import streamlit as st
import random
from utils import get_chunks, vectorize_chunks, get_relevant_chunk

def chat():
    st.subheader("💬 Childhood Law Chatbot")
    user_query = st.text_input("உங்கள் கேள்வியை தமிழில் எழுதவும்:")
    
    if st.button("Send"):
        chunks = get_chunks()
        vectors = vectorize_chunks(chunks)
        relevant = get_relevant_chunk(user_query, chunks, vectors)
        response = f"🔎 உரிய சட்ட விவரம்:\n{relevant}"
        st.text_area("பதில்:", response, height=200)

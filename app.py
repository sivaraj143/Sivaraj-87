import streamlit as st
from auth import login, signup, edit_profile
from chatbot_engine import chat
from history import view_history

st.title("👶🏽 Childhood Law Chatbot (Tamil Nadu)")
menu = ["Login", "Signup", "Chat", "History", "Edit Profile"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Signup":
    signup()
elif choice == "Login":
    login()
elif choice == "Chat":
    chat()
elif choice == "History":
    view_history()
elif choice == "Edit Profile":
    edit_profile()

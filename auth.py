import streamlit as st
import sqlite3

def create_user_table():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS user
                 (username TEXT, password TEXT)''')
    conn.commit()
    conn.close()

def signup():
    create_user_table()
    st.subheader("Signup")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")
    if st.button("Create Account"):
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("INSERT INTO user (username, password) VALUES (?,?)", (user, pwd))
        conn.commit()
        st.success("Account created!")

def login():
    st.subheader("Login")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")
    if st.button("Login"):
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("SELECT * FROM user WHERE username=? AND password=?", (user, pwd))
        if c.fetchone():
            st.success(f"Welcome {user}!")
        else:
            st.error("Invalid credentials")

def edit_profile():
    st.subheader("Edit Profile (Under Development)")

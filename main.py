import streamlit as st

st.title("CS 7641 Group 27 Project Solafune")

f = open("content.md")
with open("content.md") as f:
    content = f.read()

st.write(content)
import streamlit as st
from backend.agents import ChiefEditorAgent
st.write("Perplexity Clone")

task= {
    "query": "What is the best way to lose weight?",
    "verbose": True
}

chief_editor = ChiefEditorAgent(task=task)


prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
st.write("Outside the form")
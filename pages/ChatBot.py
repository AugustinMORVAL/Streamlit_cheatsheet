import streamlit as st
import yaml
from utils.tutorial_display import full_display

with open('data/chatbot.yaml', 'r') as file:
    chatbot_elements = yaml.safe_load(file)

def chatbot_page():
    st.title("Streamlit ChatBot Components")
    st.markdown("This page demonstrates the various components used to build a chatbot interface in Streamlit. Each component is explained and has a code snippet that you can use in your own apps.")

    category = st.selectbox("Filter by Category", ["All", "Chat Message", "Input", "Interaction", "History"])

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    global_vars = {
        "st": st,
        "messages": st.session_state.messages
    }

    if category == "All":
        full_display(chatbot_elements, global_vars)
    else:
        filtered_elements = [e for e in chatbot_elements if e.get('category', '') == category]
        full_display(filtered_elements, global_vars)

if __name__ == "__main__":
    chatbot_page()
import streamlit as st
import yaml
from utils.tutorial_display import full_display

with open('data/state_management.yaml', 'r') as file:
    state_management_elements = yaml.safe_load(file)

def state_management_page():
    st.title("Streamlit State Management")
    st.markdown("""
    State management in Streamlit is crucial for creating interactive and dynamic applications. 
    This tutorial will cover the basics of using `st.session_state` to manage your app's state.
    """)

    full_display(state_management_elements, {"st": st})

if __name__ == "__main__":
    state_management_page()
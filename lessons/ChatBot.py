import streamlit as st
import yaml
from utils.tutorial_display import TutorialDisplay

def chatbot_page():
    tutorial = TutorialDisplay(
        page_title="Streamlit ChatBot Components",
        page_description="This page demonstrates the various components used to build a chatbot interface in Streamlit. Each component is explained and has a code snippet that you can use in your own apps."
    )
    
    tutorial.load_yaml('data/chatbot.yaml')
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    global_vars = {
        "st": st,
        "messages": st.session_state.messages
    }
    tutorial.set_global_vars(global_vars)
    
    practice_content = {
        "description": """
        Create a simple chatbot interface:
        1. Initialize a chat history using session state
        2. Add a text input for user messages
        3. Display chat messages in a conversation format
        4. Add a button to clear the chat history
        5. Implement a simple response mechanism
        """,
        "code_template": """
import streamlit as st

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Add assistant response
    with st.chat_message("assistant"):
        response = f"Echo: {prompt}"  # Simple echo response
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

# Clear chat button
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()
        """,
        "interactive_form": lambda: st.text_area("Write your code here"),
        "on_submit": lambda: st.success("Great job! You've created a chatbot interface!")
    }
    
    tutorial.display(practice_content)

if __name__ == "__main__":
    chatbot_page()
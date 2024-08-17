import streamlit as st
import random
from utils.tutorial_display import full_display

chat_elements = [
    {
        "label": "User Greeting",
        "code_snippet": '''
with st.chat_message("assistant"):
    st.write("Hello 👋")
''',
        "explanation": "This is a simple greeting message from the user."
    },
    {
        "label": "Chat Input",
        "code_snippet": '''
with st.container():
    st.chat_input("Say something", key="chat_input")
''',
        "explanation": "This is a chat input widget where users can type their messages."
    },
    {
        "label": "Chatbot Response",
        "code_snippet": '''
if prompt := st.chat_input("What is up?", key="chatbot_response"):
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = "Hello! I'm a simple chatbot. You said: " + prompt
        message_placeholder.markdown(full_response)
''',
        "explanation": "This is how the chatbot responds to user input."
    },
    {
        "label": "User Response",
        "code_snippet": '''
if prompt := st.chat_input("What is up?", key="user_response"):
    with st.chat_message("user"):
        message_placeholder = st.empty()
        full_response = "User : " + prompt
        message_placeholder.markdown(full_response)
''',
        "explanation": "This is how the chatbot responds to user input."
    }
]

responses = {
"hello": ["Hi!", "Hello!", "Hey there!"],
"how are you": ["I'm just a bot, but I'm here to help!", "I'm good, thanks for asking!"],
"bye": ["Goodbye!", "See you later!"]
}

def generate_response(user_input):
    user_input = user_input.lower()
    for key in responses.keys():
        if key in user_input:
            return random.choice(responses[key])
    return "I'm not sure how to respond to that."

def chatting_app():

    st.title("ChatBot Application")
    full_display(chat_elements)
    
    st.title("Example of ChatBot")
    st.subheader("Chatbot Simple Response")

    with st.chat_message("assistant"):
        st.write("Hello 👋")
    with st.container():
        st.write("Hello 👋")
        if prompt := st.chat_input("What is up?", key="example_chat input"):
            with st.chat_message("user"):
                message_placeholder = st.empty()
                full_response = prompt
                message_placeholder.markdown(full_response)
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = generate_response(prompt) 
                message_placeholder.markdown(full_response)
    
    if st.toggle("Show code"):
        code_snippet = """
        with st.chat_message("assistant"):
            st.write("Hello 👋")

        with st.container():
            if prompt := st.chat_input("What is up?", key="example_chat_input"):
                with st.chat_message("user"):
                    message_placeholder = st.empty()
                    full_response = prompt
                    message_placeholder.markdown(full_response)

                with st.chat_message("assistant"):
                    message_placeholder = st.empty()
                    full_response = generate_response(prompt) # Replace this with your chatbot logic
                    message_placeholder.markdown(full_response)

        if st.toggle("Show code"):
            st.code(code_snippet, language='python')
        """
        st.code(code_snippet, language='python')
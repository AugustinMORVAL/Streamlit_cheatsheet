import streamlit as st
import yaml
from utils.tutorial_display import TutorialDisplay

def state_management_page():

    tutorial = TutorialDisplay(
        page_title="Streamlit State Management",
        page_description="State management in Streamlit is crucial for creating interactive and dynamic applications. This tutorial will cover the basics of using `st.session_state` to manage your app's state."
    )
    
    tutorial.load_yaml('data/state_management.yaml')
    
    tutorial.set_global_vars({"st": st})
    
    practice_content = {
        "description": """
        Create a simple app that demonstrates state management:
        1. Use `st.session_state` to store a counter
        2. Add buttons to increment and decrement the counter
        3. Display the current value of the counter
        4. Add a reset button that sets the counter back to 0
        """,
        "code_template": """
import streamlit as st

# Initialize counter in session state if it doesn't exist
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# Display current counter value
st.write(f"Current count: {st.session_state.counter}")

# Add buttons to modify counter
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Increment"):
        st.session_state.counter += 1

with col2:
    if st.button("Decrement"):
        st.session_state.counter -= 1

with col3:
    if st.button("Reset"):
        st.session_state.counter = 0
        """,
        "interactive_form": lambda: st.text_area("Write your code here"),
        "on_submit": lambda: st.success("Great job! You've implemented state management!")
    }
    
    tutorial.display(practice_content)

if __name__ == "__main__":
    state_management_page()
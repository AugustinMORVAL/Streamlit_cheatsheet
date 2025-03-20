import streamlit as st
import yaml
from utils.tutorial_display import TutorialDisplay
import time

def layout_page():
    tutorial = TutorialDisplay(
        page_title="Streamlit Layout & Containers",
        page_description="This page demonstrates various layout and container components in Streamlit. Learn how to organize your app's content using columns, containers, expanders, and more."
    )
    
    tutorial.load_yaml('data/layout.yaml')
    
    global_vars = {
        "st": st,
        "time": time
    }
    tutorial.set_global_vars(global_vars)
    
    practice_content = {
        "description": """
        Create a dashboard layout using Streamlit's layout components:
        1. Create a sidebar with navigation options
        2. Use columns to organize content in the main area
        3. Add an expander for additional information
        4. Include a container for dynamic content
        5. Use tabs to organize different sections
        """,
        "code_template": """
import streamlit as st

# Sidebar navigation
with st.sidebar:
    st.title("Navigation")
    page = st.radio("Go to", ["Home", "Data", "Settings"])

# Main content
st.title("My Dashboard")

# Columns for main content
col1, col2 = st.columns(2)

with col1:
    st.header("Section 1")
    st.write("This is the first section")
    
    # Expander for additional info
    with st.expander("See more"):
        st.write("This is additional information")

with col2:
    st.header("Section 2")
    st.write("This is the second section")
    
    # Container for dynamic content
    with st.container():
        st.write("This content can be updated dynamically")

# Tabs for different views
tab1, tab2 = st.tabs(["Overview", "Details"])

with tab1:
    st.write("Overview content")

with tab2:
    st.write("Detailed information")
        """,
        "interactive_form": lambda: st.text_area("Write your code here"),
        "on_submit": lambda: st.success("Great job! You've created a well-organized dashboard layout!")
    }
    
    tutorial.display(practice_content)

if __name__ == "__main__":
    layout_page() 
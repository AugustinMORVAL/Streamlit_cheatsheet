import streamlit as st
from pages_registry import get_pages
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Streamlit CheatSheet",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        margin: 0.2rem 0;
        padding: 0.5rem;
        border-radius: 0.5rem;
    }
    .sidebar .sidebar-content {
        background-color: #f0f2f6;
        padding: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state['page'] = 'Home'

# Sidebar
with st.sidebar:
    st.title("📚 Streamlit CheatSheet")
    st.markdown("---")
    
    pages = get_pages()
    
    for page_name in ["Home", "Installation"]:
        if st.button(page_name, key=f"nav_{page_name}"):
            st.session_state['page'] = page_name
    
    st.markdown("##### Core Features")
    core_pages = ["Widgets & Input", "Display Elements", "Layout & Containers", 
                 "State Management", "Status", "Placeholder & Help"]
    for page_name in core_pages:
        if st.button(page_name, key=f"nav_{page_name}"):
            st.session_state['page'] = page_name
    
    st.markdown("##### Examples & Tutorials")
    tutorial_pages = ["Build a ChatBot"]
    for page_name in tutorial_pages:
        if st.button(page_name, key=f"nav_{page_name}"):
            st.session_state['page'] = page_name
            
    st.markdown("##### Extra")
    extra_pages = ["Stqdm"]
    for page_name in extra_pages:
        if st.button(page_name, key=f"nav_{page_name}"):
            st.session_state['page'] = page_name
    
    st.markdown("---")
    st.markdown("### Resources")
    st.markdown("""
    - [Streamlit Docs](https://docs.streamlit.io)
    - [GitHub Repository](https://github.com/streamlit/streamlit)
    - [Community Forum](https://discuss.streamlit.io)
    """)

# Main content
## TO DO : think about main content if needed

# Display the selected page
pages[st.session_state['page']]()
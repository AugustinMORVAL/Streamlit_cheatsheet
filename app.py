import streamlit as st
from resources.home import main_page
from resources.install import installation_page
from resources.widget import widget_page
from resources.display import display_page
from resources.placeholder import placeholder_page
from resources.chat_app import chatting_app

pages = {
    "Home": main_page,
    "Installation": installation_page,
    "Display": display_page,
    "Widgets": widget_page,
    "Placeholder": placeholder_page,
    "Build a ChatBot": chatting_app,
}

# Set "Home" as the default page
if 'page' not in st.session_state:
    st.session_state.page = "Home"

st.logo("img/logo-Cyy6uKYt.png")
st.image("img/streamlit-logo-primary-colormark-darktext.png", use_column_width=True)

st.sidebar.title("Navigation Menu")
for page_title, page_func in pages.items():
    if st.sidebar.button(f"{page_title}"):
        st.session_state.page = page_title

# Display the selected page
page_func = pages[st.session_state.page]
page_func()
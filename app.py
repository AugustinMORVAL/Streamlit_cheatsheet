import streamlit as st
from utils.pages_registry import get_pages

st.set_page_config(
    page_title="Streamlit Cheatsheet",
    page_icon="📚",
)

st.sidebar.image("assets/images/streamlit-logo-primary-colormark-darktext.png", use_column_width=True)

if 'page' not in st.session_state:
    st.session_state['page'] = 'Home'

pages = get_pages()

page = st.sidebar.selectbox('Go to', list(pages.keys()))


st.session_state['page'] = page
pages[st.session_state['page']]()

# Footer
st.markdown("""
<div style="text-align: center;">
© 2024 Morval Tech. All rights reserved.
</div>
""", unsafe_allow_html=True)
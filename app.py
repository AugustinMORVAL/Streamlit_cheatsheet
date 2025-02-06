import streamlit as st
from pages_registry import get_pages

st.set_page_config(
    page_title="Streamlit Cheatsheet",
    page_icon="📚",
)

if 'page' not in st.session_state:
    st.session_state['page'] = 'Home'

pages = get_pages()

# Remplacer le selectbox par des boutons
for page_name in pages.keys():
    if st.sidebar.button(page_name):
        st.session_state['page'] = page_name

pages[st.session_state['page']]()

# Footer
st.markdown("""
<div style="text-align: center;">
© 2024 Morval Tech. All rights reserved.
</div>
""", unsafe_allow_html=True)
import streamlit as st

def full_display(label : str, code_snippet : str, explanation : str):
    st.subheader(label)
    col1, col2 = st.columns(2)
    with col1:
        locals().update({'key': label})
        exec(code_snippet, locals())
    with col2:
        st.markdown(explanation)
        if st.toggle("Show code", key=label):
            st.code(code_snippet, language='python')

def display_code(label : str, code_snippet : str, explanation : str): 
    col1, col2 = st.columns(2)
    st.subheader(label)
    with col1: 
        st.code(code_snippet, language='python')
    with col2:
        st.markdown(explanation)

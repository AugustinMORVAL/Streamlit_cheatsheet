import streamlit as st

def full_display(label : str, function, *args, explanation : str):
    st.subheader(label)
    col1, col2 = st.columns(2)
    with col1:
        getattr(st.empty(), function)(*args)
    with col2:
        st.markdown(explanation)
        if st.toggle("Show code", key=label):
            st.code(f"st.{function}({', '.join(map(repr, args))})", language='python')
    

def display_code(label : str, code_snippet : str, explanation : str): 
    col1, col2 = st.columns(2)
    st.subheader(label)
    with col1: 
        st.code(code_snippet, language='python')
    with col2:
        st.markdown(explanation)

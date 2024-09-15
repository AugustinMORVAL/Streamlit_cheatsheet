import streamlit as st

def full_display(displayed_functions: list[dict], global_vars: dict):
    for i, item in enumerate(displayed_functions):
        label = f"{i+1}. {item['label']}"
        code_snippet = item['code_snippet']
        explanation = item['explanation']
        data = item.get('data', None)
        alt = item.get('alt', None)
        try:
            st.subheader(label)
            col1, col2 = st.columns(2)
            with col1:
                exec_globals = global_vars.copy()
                exec_globals.update({"data": data})
                exec(code_snippet, exec_globals)
            with col2:
                st.markdown(explanation)
                if st.toggle("Show code", key=label):
                    if alt:
                        st.code(alt, language='python')
                    else:
                        st.code(code_snippet, language='python')
        except Exception as e:
            st.error(f"An error occurred: {e}")

def display_code(label : str, code_snippet : str, explanation : str): 
    col1, col2 = st.columns(2)
    st.subheader(label)
    with col1: 
        st.code(code_snippet, language='python')
    with col2:
        st.markdown(explanation)

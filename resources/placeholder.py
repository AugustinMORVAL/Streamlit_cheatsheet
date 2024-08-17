import streamlit as st
import pandas as pd
from utils.tutorial_display import full_display

data = {
    'Column1': [1, 2, 3, 4, 5],
    'Column2': ['A', 'B', 'C', 'D', 'E']
}
df = pd.DataFrame(data)

path_to_logo = "img/logo-Cyy6uKYt.png"

placeholder_elements = [
    {
       "label": "Placeholder Text",
       "code_snippet": "st.empty().text('Hello, World!')",
       "explanation": "Displays text that can be updated later.",
       "alt": "placeholder.text('Hello, World!')",
    },
    {
       "label": "Placeholder DataFrame",
       "code_snippet": "st.empty().dataframe(data)",
       "explanation": "Displays a DataFrame that can be updated later.",
       "data": df,
       "alt": "placeholder.dataframe(df)"
    },
    {
       "label": "Placeholder Line Chart",
       "code_snippet": "st.empty().line_chart(data)",
       "explanation": "Displays a line chart that can be updated later.",
       "data": df,
       "alt": "placeholder.linechart(df)"
    },
    {
       "label": "Placeholder Image",
       "code_snippet": "st.empty().image(data)",
       "explanation": "Displays an image that can be updated later.",
       "data": path_to_logo,
       "alt": "placeholder.image(path_to_logo)"
    },
    {
       "label": "Placeholder Markdown",
       "code_snippet": "st.empty().markdown('# Hello, *World!*')",
       "explanation": "Displays Markdown text that can be updated later.",
       "alt": "placeholder.markdown('# Hello, *World!*')",
    },
    {
       "label": "Placeholder Write",
       "code_snippet": "st.empty().write(data)",
       "explanation": "Displays any type of data that can be updated later.",
       "data": df,
       "alt": "placeholder.write(df)"
    },
]


def placeholder_page():
    st.title("Streamlit Placeholder, Help, and Options Widgets")
    st.markdown("This page demonstrates all the Streamlit placeholder widgets and help. Each widget is explained and has a code snippet that you can use in your own apps.")
    st.title("Placeholder")

    st.code(f"placeholder = st.empty()", language='python')
    placeholder = st.empty()
    full_display(placeholder_elements)
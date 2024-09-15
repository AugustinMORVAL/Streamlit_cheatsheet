import streamlit as st
import pandas as pd
import yaml
from utils.tutorial_display import full_display

data = pd.DataFrame({
    'col1': [1, 2, 3, 4],
    'col2': [10, 20, 30, 40]
})

url = "https://www.example.com"

with open('data/widgets.yaml', 'r') as file:
    widgets = yaml.safe_load(file)

for widget in widgets:
    if widget['label'] == 'Link Button':
        widget['data'] = url
    elif widget['label'] == 'Data Editor':
        widget['data'] = data

def widget_page():
    st.title("Streamlit Interactive Widgets")
    st.markdown("This page demonstrates all the Streamlit interactive widgets. Each widget is explained and has a code snippet that you can use in your own apps.")

    global_vars = {
        # Librairies
        "st": st,
        "pd": pd,
        
        # Data
        "data": data,
        "url": url,
    }

    full_display(widgets, global_vars)

if __name__ == "__main__":
    widget_page()


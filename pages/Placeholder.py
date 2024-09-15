import streamlit as st
import pandas as pd
import yaml
from utils.tutorial_display import full_display

data = {
    'Column1': [1, 2, 3, 4, 5],
    'Column2': ['A', 'B', 'C', 'D', 'E']
}
df = pd.DataFrame(data)

path_to_logo = "img/logo-Cyy6uKYt.png"

# Load placeholder elements from YAML file
with open('data/placeholder.yaml', 'r') as file:
    placeholder_elements = yaml.safe_load(file)

# Preprocess placeholder elements
for element in placeholder_elements:
    if element['label'] == 'Placeholder DataFrame' or element['label'] == 'Placeholder Line Chart' or element['label'] == 'Placeholder Write':
        element['data'] = df
    elif element['label'] == 'Placeholder Image':
        element['data'] = path_to_logo

def placeholder_page():
    st.title("Streamlit Placeholder, Help, and Options Widgets")
    st.markdown("This page demonstrates all the Streamlit placeholder widgets and help. Each widget is explained and has a code snippet that you can use in your own apps.")

    category = st.selectbox("Filter by Category", ["All", "Placeholder", "Help"])

    global_vars = {
        # Libraries
        "st": st,
        "pd": pd,
        
        # Data
        "df": df,
        "path_to_logo": path_to_logo,
        
        # Additional variables that might be used in placeholders
        "placeholder": st.empty(),
    }

    if category == "All":
        full_display(placeholder_elements, global_vars)
    else:
        filtered_elements = [e for e in placeholder_elements if e.get('category', '') == category]
        full_display(filtered_elements, global_vars)

if __name__ == "__main__":
    placeholder_page()
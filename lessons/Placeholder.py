import streamlit as st
import pandas as pd
import yaml
from utils.tutorial_display import TutorialDisplay

def placeholder_page():
    
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 28, 22],
        'City': ['New York', 'London', 'Paris', 'Tokyo', 'Berlin']
    })
    
    path_to_logo = "assets/img/logo-Cyy6uKYt.png"
    
    tutorial = TutorialDisplay(
        page_title="Streamlit Placeholder, Help, and Options Widgets",
        page_description="This page demonstrates all the Streamlit placeholder widgets and help. Each widget is explained and has a code snippet that you can use in your own apps."
    )
    
    tutorial.load_yaml('data/placeholder.yaml')
    
    global_vars = {
        # Libraries
        "st": st,
        "pd": pd,
        
        # Data
        "df": df,
        "path_to_logo": path_to_logo,
        
        # Placeholder
        "placeholder": st.empty(),
    }
    tutorial.set_global_vars(global_vars)
    
    practice_content = {
        "description": """
        Create a simple app that demonstrates placeholder usage:
        1. Create a placeholder for a chart
        2. Add a button that updates the chart with different data
        3. Use a placeholder to show/hide content
        4. Add a help tooltip to explain the functionality
        """,
        "code_template": """
import streamlit as st
import pandas as pd

# Create a placeholder for the data
data_placeholder = st.empty()

# Create initial data
df = pd.DataFrame({
    'Product': ['Apples', 'Bananas', 'Oranges', 'Grapes', 'Pears'],
    'Price': [1.20, 0.50, 0.80, 2.00, 1.50],
    'Stock': [100, 150, 75, 50, 125]
})

# Display initial data
data_placeholder.dataframe(df)

# Add a button to update the data
if st.button("Update Prices"):
    # Update prices with some random changes
    import random
    df['Price'] = [round(p * random.uniform(0.8, 1.2), 2) for p in df['Price']]
    data_placeholder.dataframe(df)

# Add a help tooltip
st.help(st.empty)
        """,
        "interactive_form": lambda: st.text_area("Write your code here"),
        "on_submit": lambda: st.success("Great job! You've implemented placeholders!")
    }
    
    tutorial.display(practice_content)

if __name__ == "__main__":
    placeholder_page()
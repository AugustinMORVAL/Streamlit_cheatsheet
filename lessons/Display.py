import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import plotly.express as px
import random
import yaml
from utils.tutorial_display import TutorialDisplay
import os

def initialize_display_data():
    """Initialize sample data and charts for display examples"""
    # Sample DataFrame
    df = pd.DataFrame({
        'lat': np.random.randn(100) * 0.5 + 37.76,
        'lon': np.random.randn(100) * 0.5 + -122.4
    })
    
    # Sample charts
    try:
        # Altair chart
        chart_data = pd.DataFrame({
            'date': pd.date_range('2024-01-01', periods=30),
            'value': np.random.randn(30).cumsum(),
            'category': np.random.choice(['A', 'B', 'C'], 30)
        })
    except Exception as e:
        st.error(f"Error creating Altair chart: {e}")
        chart = None
    
    try:
        # Matplotlib chart
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3, 4])
        plt.close(fig)
    except Exception as e:
        st.error(f"Error creating Matplotlib chart: {e}")
        fig = None
    
    return {
        'df': df,
        'chart_data': chart_data,
        'fig': fig
    }

def my_generator():
    i = 0
    while i < 5:
        i += 1  
        yield f'Data point {i}: {random.randint(1, 100),}'

def my_llm_stream(prompt):
    for word in prompt.split():
        yield word

def display_page():
    tutorial = TutorialDisplay(
        page_title="Streamlit Display Functions",
        page_description="Learn how to display various types of content in your Streamlit app. Each example shows both the code and its output."
    )

    display_data = initialize_display_data()
    
    try:
        tutorial.load_yaml('data/display.yaml')
    except Exception as e:
        st.error(f"Error loading display elements: {e}")
    
    global_vars = {
        # Libraries
        "st": st,
        "pd": pd,
        "np": np,
        "alt": alt,
        "plt": plt,
        "px": px,
        "random": random,
        
        # Data and charts
        "df": display_data['df'],
        "chart_data": display_data['chart_data'],
        "fig": display_data['fig'],
        
        # Helper functions
        "my_generator": my_generator,
        "my_llm_stream": my_llm_stream
    }
    tutorial.set_global_vars(global_vars)
    
    practice_content = {
        "description": """
        Try creating a simple dashboard that combines different display elements:
        1. Create a DataFrame with some sample data
        2. Display it using `st.dataframe()`
        3. Create a chart using any of the charting libraries
        4. Add some text elements using markdown
        5. Organize everything using columns and containers
        """,
        "code_template": """
# Your code here
import streamlit as st
import pandas as pd
import numpy as np

# Create sample data
df = pd.DataFrame({
    'A': np.random.randn(5),
    'B': np.random.randn(5)
})

# Display the data
st.dataframe(df)

# Create a chart
st.line_chart(df)

# Add some text
st.markdown("## My Dashboard")
st.write("This is a sample dashboard!")
        """,
        "interactive_form": lambda: st.text_area("Write your code here"),
        "on_submit": lambda: st.success("Great job! You've created a dashboard!")
    }
    
    tutorial.display(practice_content)

if __name__ == "__main__":
    display_page()
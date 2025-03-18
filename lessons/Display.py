import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import plotly.express as px
import random
import yaml
from utils.tutorial_display import full_display
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
        chart = alt.Chart(df).mark_circle().encode(
            x='lat',
            y='lon',
            size='value:Q',
            color='value:Q',
            tooltip=['lat', 'lon']
        ).properties(width=400, height=300)
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
        'chart': chart,
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
    st.set_page_config(layout="wide")
    
    # Page header
    st.title("📊 Display Elements")
    st.markdown("""
        Learn how to display various types of content in your Streamlit app.
        Each example shows both the code and its output.
    """)
    
    # Initialize display data
    display_data = initialize_display_data()
    
    # Load display elements from YAML
    try:
        with open('data/display.yaml', 'r') as file:
            display_elements = yaml.safe_load(file)
    except Exception as e:
        st.error(f"Error loading display elements: {e}")
        display_elements = []
    
    # Display tutorial content
    full_display(display_elements, display_data)
    
    # Interactive exercise section
    st.markdown("---")
    st.header("🎯 Practice Exercise")
    st.markdown("""
        Try creating a simple dashboard that combines different display elements:
        1. Create a DataFrame with some sample data
        2. Display it using `st.dataframe()`
        3. Create a chart using any of the charting libraries
        4. Add some text elements using markdown
        5. Organize everything using columns and containers
    """)
    
    # Add a code editor for practice
    if st.toggle("Show code editor"):
        st.code("""
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
        """, language='python')

if __name__ == "__main__":
    display_page()
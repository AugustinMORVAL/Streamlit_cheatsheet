import streamlit as st
import pandas as pd
import yaml
from utils.tutorial_display import TutorialDisplay

data = pd.DataFrame({
    'col1': [1, 2, 3, 4],
    'col2': [10, 20, 30, 40]
})

url = "https://www.example.com"

def widget_page():
    
    tutorial = TutorialDisplay(
        page_title="Streamlit Interactive Widgets",
        page_description="This page demonstrates all the Streamlit interactive widgets. Each widget is explained and has a code snippet that you can use in your own apps."
    )
    
    tutorial.load_yaml('data/widgets.yaml')
    
    global_vars = {
        # Libraries
        "st": st,
        "pd": pd,
        
        # Data
        "data": data,
        "url": url,
    }
    tutorial.set_global_vars(global_vars)
    
    practice_content = {
        "description": """
        Create a pizza ordering form using Streamlit widgets:
        1. Add a text input for the customer's name
        2. Create a multiselect for toppings (e.g., mushrooms, pepperoni, olives)
        3. Add a slider for pizza size (8 to 16 inches)
        4. Include a radio button for crust type (thin, regular, thick)
        5. Add a checkbox for extra cheese
        6. Create a number input for quantity (1-5)
        7. Add a submit button that displays the order summary
        """,
        "code_template": """
import streamlit as st

st.title("🍕 Pizza Order Form")

# Customer name
name = st.text_input("Your Name")

# Pizza toppings
toppings = st.multiselect(
    "Choose your toppings:",
    ["Pepperoni", "Mushrooms", "Olives", "Onions", "Bell Peppers", "Extra Cheese"]
)

# Pizza size
size = st.slider("Pizza Size (inches)", 8, 16, 12)

# Crust type
crust = st.radio("Choose your crust:", ["Thin", "Regular", "Thick"])

# Extra cheese
extra_cheese = st.checkbox("Add extra cheese")

# Quantity
quantity = st.number_input("Number of Pizzas", 1, 5)

# Submit button
if st.button("Place Order"):
    # Display order summary
    st.write("### Order Summary")
    st.write(f"Customer: {name}")
    st.write(f"Size: {size} inches")
    st.write(f"Crust: {crust}")
    st.write(f"Toppings: {', '.join(toppings)}")
    st.write(f"Extra Cheese: {'Yes' if extra_cheese else 'No'}")
    st.write(f"Quantity: {quantity}")
        """,
        "interactive_form": lambda: st.text_area("Write your code here"),
        "on_submit": lambda: st.success("Great job! You've created an interactive pizza order form!")
    }
    
    tutorial.display(practice_content)

if __name__ == "__main__":
    widget_page()


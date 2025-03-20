import streamlit as st
import yaml
import time
from stqdm import stqdm
import pandas as pd
from utils.tutorial_display import TutorialDisplay

def stqdm_page():
    """Initialize the stqdm page with tutorial display"""

    intro_section = {
        'title': '## Install stqdm',
        'content': """
        Streamlit-tqdm is a Streamlit component that provides a progress bar for your Streamlit app.
        Beforehand, you need to install stqdm. To install stqdm, you can use the following command:
        """,
        'code': """
            pip install stqdm
        """,
        'language': 'python',
        'additional_content': """
        After installation, import stqdm in your script:
        """,
        'additional_code': """
            from stqdm import stqdm
        """,
        'additional_language': 'python'
    }
    
    tutorial = TutorialDisplay(
        page_title="Streamlit-tqdm",
        page_description="Learn about Streamlit-tqdm, a Streamlit component that provides a progress bar for your Streamlit app.",
        intro_section=intro_section
    )
    
    tutorial.load_yaml('data/stqdm.yaml')
    
    tutorial.set_global_vars({
        'st': st,
        'time': time,
        'stqdm': stqdm,
        'pd': pd
    })
    
    tutorial.display() 

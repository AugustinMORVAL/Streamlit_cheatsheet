import streamlit as st
import yaml
from utils.tutorial_display import TutorialDisplay

def insert_page_name_here():
    """insert description here"""

    intro_section = {
        'title': '## insert intro title here',
        'content': """
        insert intro content here
        """,
        'code': """
            insert code here
        """,
        'language': 'python'
    }
    
    tutorial = TutorialDisplay(
        page_title="insert page title here",
        page_description="insert page description here",
        intro_section=intro_section
    )
    
    tutorial.load_yaml('data/insert yaml file here')
    
    tutorial.set_global_vars({
        'insert global variables here' : 'insert global variables here'
    })
    
    tutorial.display() 

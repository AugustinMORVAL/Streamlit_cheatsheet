import streamlit as st
import yaml
import time
from utils.tutorial_display import TutorialDisplay

def status_page():
    """Initialize the status page with tutorial display"""
    tutorial = TutorialDisplay(
        page_title="Status Elements",
        page_description="Learn about Streamlit's status indicators, feedback messages, and animations."
    )
    
    tutorial.load_yaml('data/status.yaml')

    tutorial.set_global_vars({
        'st': st,
        'time': time
    })
    
    # Practice content
    practice_content = {
        'description': """
        Create a Streamlit app that simulates a data processing pipeline with the following features:
        1. A button to start the process
        2. A status container showing the current step
        3. Progress bar for each step
        4. Success/error messages for completion/failure
        5. Celebration animation when complete
        """,
        'code_template': """
        # Your code here
        if st.button("Start Processing"):
            with st.status("Processing data..."):
                # Step 1: Loading
                st.write("Loading data...")
                st.progress(25)
                time.sleep(1)
                
                # Step 2: Processing
                st.write("Processing data...")
                st.progress(50)
                time.sleep(1)
                
                # Step 3: Saving
                st.write("Saving results...")
                st.progress(75)
                time.sleep(1)
                
                # Step 4: Complete
                st.write("Complete!")
                st.progress(100)
                time.sleep(1)
                
            st.success("Data processing completed successfully!")
            st.balloons()
        """,
        'interactive_form': lambda: None,
        'on_submit': lambda: None
    }
    
    # Display the tutorial
    tutorial.display(practice_content) 
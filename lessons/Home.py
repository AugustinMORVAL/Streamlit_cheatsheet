import streamlit as st
import streamlit.components.v1 as components

def main_page():
    st.title("Welcome to Streamlit CheatSheet")
        
    # Introduction
    st.markdown("""
    ## 🚀 What is Streamlit?
    
    Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. In just a few minutes you can build and deploy powerful data apps.
    
    ### Key Features:
    - 🎨 Beautiful, interactive UI components
    - 📊 Built-in support for data visualization
    - 🔄 Hot-reloading for instant updates
    - 🎯 Easy deployment options
    - 🛠️ Rich ecosystem of components
    """)
    
    # Quick Start
    st.markdown("""
    ## ⚡ Quick Start
    
    ```python
    import streamlit as st
    
    st.title('Hello World!')
    st.write('Welcome to my first Streamlit app!')
    ```
    """)
    
    # Learning Path
    st.markdown("""
    ## 📚 Learning Path
    
    Follow this structured path to master Streamlit:
    
    1. **Getting Started**
       - Installation and setup
       - Basic app structure
    
    2. **Core Concepts**
       - Widgets and input elements
       - Display elements
       - Data visualization
       - State management
    
    3. **Examples & Projects**
       - ChatBot development
       - Data analysis apps
       - Machine learning demos
    """)
    
    # Interactive Demo
    st.markdown("""
    ## 🎮 Interactive Demo
    
    Try this simple example to see Streamlit in action:
    """)
    
    with st.expander("Click to see the demo"):
        name = st.text_input("Enter your name")
        if name:
            st.write(f"Hello, {name}! 👋")
            
            age = st.slider("Select your age", 0, 100, 25)
            st.write(f"You are {age} years old!")
            
            if st.button("Generate a random number"):
                import random
                st.write(f"Your random number is: {random.randint(1, 100)}")
    
    # Resources
    st.markdown("""
    ## 📖 Additional Resources
    
    - [Official Documentation](https://docs.streamlit.io)
    - [Streamlit Gallery](https://streamlit.io/gallery)
    - [Community Forum](https://discuss.streamlit.io)
    - [GitHub Repository](https://github.com/streamlit/streamlit)
    
    ## 🎯 Next Steps
    
    1. Check out the **Installation** guide to set up your environment
    2. Explore the **Widgets & Input** section to learn about interactive elements
    3. Visit the **Examples** section to see real-world applications
    """)
    
    # Feedback
    st.markdown("""
    ## 💡 Feedback
    
    Help us improve this tutorial by providing your feedback:
    """)
    
    with st.form("feedback_form"):
        rating = st.slider("Rate this tutorial", 1, 5, 3)
        feedback = st.text_area("Share your thoughts")
        submitted = st.form_submit_button("Submit Feedback")
        
        if submitted:
            st.success("Thank you for your feedback! 🙏")
            
    # Author info
    st.markdown("""
    ---
    ### 👨‍💻 About the Author
    
    This Streamlit CheatSheet was created by [Augustin MORVAL](https://github.com/AugustinMORVAL), a self-taught developer and tech enthusiast. 
    
    [![GitHub](https://img.shields.io/badge/GitHub-AugustinMORVAL-blue?style=flat&logo=github)](https://github.com/AugustinMORVAL)
    [![LinkedIn](https://img.shields.io/badge/LinkedIn-Augustin_MORVAL-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/augustin-morval)
    
    *Part of my [Streamlit_cheatsheet](https://github.com/AugustinMORVAL/Streamlit_cheatsheet) project - An interactive Streamlit tutorial built with Streamlit itself.*
    
    ---
    """)
    
if __name__ == "__main__":
    main_page()
import streamlit as st

def installation_page():
    st.title("Streamlit Installation Guide")

    st.subheader("1. Install Streamlit")
    st.markdown("You can install Streamlit using pip. Open your terminal or command prompt and run the following command:")
    st.code("pip install streamlit", language='bash')

    st.subheader("2. Install Pre-release Features")
    st.markdown("If you want to try out pre-release features, you can install the nightly build of Streamlit. Uninstall the current version of Streamlit and then install the nightly build with the following commands:")
    st.code("pip uninstall streamlit", language='bash')
    st.code("pip install streamlit-nightly --upgrade", language='bash')

    st.subheader("3. Run Your First App")
    st.markdown("After installation, you can run your first Streamlit app. Create a new Python file (e.g., `first_app.py`), and add the following code:")
    st.code("""
import streamlit as st

def main():
    st.title('My First Streamlit App')
    st.write('Hello, World!')

if __name__ == "__main__":
    main()
""", language='python')

    st.markdown("Then, run the app using the following command:")
    st.code("streamlit run first_app.py", language='bash')

    st.subheader("4. Import Convention")
    st.markdown("It's a common practice to import Streamlit as `st`. This is how you can do it:")
    st.code("import streamlit as st", language='python')

    st.markdown("Now you're ready to start building your own Streamlit apps!")

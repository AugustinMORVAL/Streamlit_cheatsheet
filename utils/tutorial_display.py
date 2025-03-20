import streamlit as st
from typing import List, Dict, Any, Optional
import yaml
import numpy as np

class TutorialDisplay:
    def __init__(self, page_title: str, page_description: str, intro_section: dict = None):
        """Initialize the tutorial display with page-specific information"""
        self.page_title = page_title
        self.page_description = page_description
        self.intro_section = intro_section
        self.elements = []
        self.global_vars = {}
        self.element_counter = 0
        
    def load_yaml(self, yaml_file: str) -> None:
        """Load elements from a YAML file."""
        with open(yaml_file, 'r', encoding='utf-8') as file:
            self.elements = yaml.safe_load(file)
        
    def add_element(self, element: Dict[str, Any]) -> None:
        """Add a tutorial element to the display"""
        self.elements.append(element)
        
    def set_global_vars(self, global_vars: Dict[str, Any]) -> None:
        """Set global variables for code execution"""
        self.global_vars = global_vars
        
    def create_search_bar(self) -> List[Dict[str, Any]]:
        """Create a search bar for filtering elements"""
        search_query = st.text_input("🔍 Search examples", placeholder="Type to search...")
        if search_query:
            search_query = search_query.lower()
            return [e for e in self.elements if 
                    search_query in e.get('label', '').lower() or 
                    search_query in e.get('explanation', '').lower()]
        return self.elements

    def create_category_pills(self, elements: List[Dict[str, Any]]) -> List[str]:
        """Create pills for different categories"""
        categories = ["All"] + sorted(list(set(e.get('category', 'Uncategorized') for e in elements)))
        selected = st.pills("Categories", categories, selection_mode="multi")
        return selected

    def display_element(self, item: Dict[str, Any], index: int, category: str) -> None:
        """Display a single element with improved UI"""
        element_label = item.get('label', 'Unnamed Example').lower().replace(' ', '_')
        self.element_counter += 1
        unique_key = f"{category}_{element_label}_{self.element_counter}"
        
        if item.get('code_display', False):
            display_code(
                item.get('label', 'Unnamed Example'),
                item['code_snippet'],
                item.get('explanation', '')
            )
            return
        
        with st.container():
            st.markdown("""
                <style>
                .element-card {
                    background-color: #ffffff;
                    border-radius: 10px;
                    padding: 1rem;
                    margin: 1rem 0;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }
                </style>
            """, unsafe_allow_html=True)
            
            with st.container():
                st.markdown(f"### {index+1}. {item.get('label', 'Unnamed Example')}")
                
                # Main content
                col1, col2 = st.columns(2)
                
                with col1:
                    try:
                        exec_globals = self.global_vars.copy()
                        exec_globals['st'] = st
                        if 'data' in item:
                            exec_globals['data'] = item['data']
                        exec(item['code_snippet'], exec_globals)
                    except Exception as e:
                        st.error(f"An error occurred: {e}")
                
                with col2:
                    # Explanation and code toggle
                    st.markdown(item.get('explanation', ''))
                    if st.toggle("Show code", key=unique_key):
                        if item.get('alt'):
                            st.code(item['alt'], language='python')
                        else:
                            st.code(item['code_snippet'], language='python')

    def display_practice_section(self, practice_content: Optional[Dict[str, Any]] = None) -> None:
        """Display a practice section with customizable content"""
        st.markdown("---")
        st.header("🎯 Practice Exercise")
        
        if practice_content:
            st.markdown(practice_content.get('description', ''))
            
            if practice_content.get('code_template'):
                if st.toggle("Show code editor", key="practice_code_editor"):
                    st.code(practice_content['code_template'], language='python')
            
            if practice_content.get('interactive_form'):
                with st.expander("Click to try the exercise"):
                    with st.form("practice_exercise"):
                        practice_content['interactive_form']()
                        if st.form_submit_button("Submit"):
                            practice_content.get('on_submit', lambda: None)()

    def display(self, practice_content: Optional[Dict[str, Any]] = None, **kwargs) -> None:
        """Main display function that renders the entire tutorial"""
        # Page header
        st.title(self.page_title)
        st.markdown(self.page_description)
        
        # Introduction section
        if self.intro_section:
            st.write('---')
            if 'title' in self.intro_section:
                st.markdown(self.intro_section['title'])
            if 'content' in self.intro_section:
                st.markdown(self.intro_section['content'])
            if 'code' in self.intro_section:
                st.code(
                    self.intro_section['code'],
                    language=self.intro_section.get('language', 'python')
                )
            
            keys = set(self.intro_section.keys())
            additional_pairs = {k[:-8] for k in keys if k.endswith('_content')}
            
            for base in additional_pairs:
                content_key = f"{base}_content"
                code_key = f"{base}_code"
                language_key = f"{base}_language"
                
                if content_key in self.intro_section:
                    st.markdown(self.intro_section[content_key])
                if code_key in self.intro_section:
                    st.code(
                        self.intro_section[code_key],
                        language=self.intro_section.get(language_key, 'python')
                    )
            
            st.write('---')
        
        # Search bar
        filtered_elements = self.create_search_bar()
        
        # Categories pills
        categories = sorted(list(set(e.get('category', 'Uncategorized') for e in filtered_elements)))
        
        if len(categories) > 1:
            selected_categories = self.create_category_pills(filtered_elements)
            
            if not selected_categories:
                elements_to_show = filtered_elements
            else:
                elements_to_show = []
                for element in filtered_elements:
                    element_category = element.get('category', 'Uncategorized')
                    if element_category in selected_categories or "All" in selected_categories:
                        elements_to_show.append(element)
            
            if elements_to_show:
                unique_elements = []
                seen = set()
                for element in elements_to_show:
                    element_id = (element.get('label', ''), element.get('code_snippet', ''))
                    if element_id not in seen:
                        seen.add(element_id)
                        unique_elements.append(element)
                
                for i, element in enumerate(unique_elements):
                    category_key = "_".join(selected_categories) if selected_categories else "All"
                    self.display_element(element, i, category_key)
        else:
            for i, element in enumerate(filtered_elements):
                self.display_element(element, i, "All")
        
        if practice_content:
            self.display_practice_section(practice_content)

def display_code(label: str, code_snippet: str, explanation: str) -> None:
    """Display code-only examples with improved UI"""
    with st.container():
        st.markdown(f"### {label}")
        col1, col2 = st.columns(2)
        with col1:
            st.code(code_snippet, language='python')
        with col2:
            st.markdown(explanation)

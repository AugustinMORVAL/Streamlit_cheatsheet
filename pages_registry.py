def get_pages():
    from lessons.Home import main_page
    from lessons.Installation import installation_page
    from lessons.Widgets import widget_page
    from lessons.Display import display_page
    from lessons.Placeholder import placeholder_page
    from lessons.ChatBot import chatbot_page
    from lessons.StateManagement import state_management_page

    return {
        # Getting Started
        "Home": main_page,
        "Installation": installation_page,
        
        # Core Concepts
        "Widgets & Input": widget_page,
        "Display Elements": display_page,
        "State Management": state_management_page,
        
        # Examples & Tutorials
        "Build a ChatBot": chatbot_page,
        "Placeholder & Help": placeholder_page,
    }

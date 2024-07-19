"""
PageFactory uses the factory design pattern.
get_page_object() returns the appropriate page object.
Add elif clauses as and when you implement new pages.
"""
import importlib


class PageFactory:
    """ PageFactory uses the factory design pattern.  """

    # Mapping of page names to their respective classes
    _page_classes = {
        "main_page": "MainPage",
        "import_media": "MediaPage",
        "effect": "EffectPage",
        "edit": "EditPage",
        "timeline_settings": "TimelineSettingsPage",
        "produce": "ProducePage",
        "ai_effect": "AIEffect",
        "shortcut": "Shortcut"
    }

    @staticmethod
    def get_page_object(page_name, driver):
        # Convert the page name to lower case
        page_name = page_name.lower()

        # Get the class name from the mapping dictionary
        class_name = PageFactory._page_classes.get(page_name)

        if class_name:
            # Import the module dynamically based on the class name
            module_name = f"{page_name}"
            module = importlib.import_module(f".{module_name}", package='ATFramework_aPDR.pages')
            # Get the class from the module
            page_class = getattr(module, class_name)
            # Return an instance of the page class
            return page_class(driver)

        # Return None if the page name does not exist in the mapping
        return None

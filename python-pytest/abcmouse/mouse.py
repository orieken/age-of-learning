import importlib
import os
import time


class Mouse:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

        self.pages = {}
        self.load_pages()

    def js_locator(self, locator_parts):
        return self.driver.execute_script("".join(locator_parts))

    def navigate_to(self):
        self.driver.get(self.base_url)

    def load_pages(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        pages_dir = os.path.join(script_dir, 'pages')

        self.pages = {
            page_file: getattr(importlib.import_module(f'abcmouse.pages.{page_file}'),
                               page_file.replace('_', ' ').title().replace(' ', ''))(self.driver)
            for page_file in [filename[:-3] for filename in os.listdir(pages_dir) if
                              filename.endswith('.py') and filename != '__init__.py']
        }
        for page_name, page_instance in self.pages.items():
            setattr(self, page_name, page_instance)


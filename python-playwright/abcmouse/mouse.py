import importlib
import os
import time
from abc import ABC

import toml


class Mouse:
    def __init__(self, page):
        self.page = page

        self.urls = self.load_urls()
        self.pages = {}
        self.load_pages()

    def goto(self):
        self.page.goto(self.urls.get('base_url',''))

    def load_pages(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        pages_dir = os.path.join(script_dir, 'pages')

        self.pages = {
            page_file: getattr(importlib.import_module(f'abcmouse.pages.{page_file}'),
                               page_file
                               .replace('_', ' ')
                               .title()
                               .replace(' ', ''))(self.page, self.urls.get(page_file, ''))
            for page_file in [filename[:-3] for filename in os.listdir(pages_dir) if
                              filename.endswith('.py') and filename != '__init__.py']
        }
        for page_name, page_instance in self.pages.items():
            setattr(self, page_name, page_instance)

    def load_urls(self):
        # Get the directory of the current script (assuming it's in the same directory as config.toml)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(script_dir, 'config.toml')

        # Load URLs from the TOML file into a dictionary using the 'toml' library
        with open(config_path, 'r') as config_file:
            config_data = toml.load(config_file)

        return config_data.get('urls', {})

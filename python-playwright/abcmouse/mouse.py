import importlib
import os
import time
from abc import ABC


class Mouse:
    def __init__(self, page):
        self.page = page

        self.pages = {}
        self.load_pages()

    def goto(self):
        self.page.goto("https://www.abcmouse.com/")

    def load_pages(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        pages_dir = os.path.join(script_dir, 'pages')

        self.pages = {
            page_file: getattr(importlib.import_module(f'abcmouse.pages.{page_file}'),
                               page_file.replace('_', ' ').title().replace(' ', ''))(self.page)
            for page_file in [filename[:-3] for filename in os.listdir(pages_dir) if
                              filename.endswith('.py') and filename != '__init__.py']
        }
        for page_name, page_instance in self.pages.items():
            setattr(self, page_name, page_instance)

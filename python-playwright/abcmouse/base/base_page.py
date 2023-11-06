import time
from abc import ABC


class BasePage(ABC):
    def __init__(self, page, url=None):
        self.page = page
        self.url = url

    def wait(self, seconds):
        time.sleep(seconds)

    def navigate_to(self):
        self.page.goto(self.url)
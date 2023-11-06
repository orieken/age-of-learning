import time
from abc import ABC


class BasePage(ABC):
    def __init__(self, page):
        self.page = page

    def wait(self, seconds):
        time.sleep(seconds)

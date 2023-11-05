import time
from abc import ABC


class Page(ABC):
    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url

    def js_locator(self, locator_parts):
        return self.driver.execute_script("return " + "".join(locator_parts))

    def wait(self, seconds):
        time.sleep(seconds)

    def navigate_to(self):
        self.driver.get(self.url)
        self.wait(3)

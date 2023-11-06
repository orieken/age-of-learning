from abcmouse.base.base_page import BasePage


class LandingPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def navigate_to(self):
        self.page.goto("https://www.abcmouse.com/")

    def signup(self):
        return self.page.get_by_label("Sign Up for ABCmouse.com").locator("slot")



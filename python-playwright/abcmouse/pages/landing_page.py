from abcmouse.base.base_page import BasePage


class LandingPage(BasePage):
    def __init__(self, page, url):
        super().__init__(page, url)

    def signup(self):
        return self.page.get_by_label("Sign Up for ABCmouse.com")



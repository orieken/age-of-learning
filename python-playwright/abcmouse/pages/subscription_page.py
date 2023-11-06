from abcmouse.base.base_page import BasePage


class SubscriptionPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def navigate_to(self):
        self.page.goto("https://www.abcmouse.com/abc/subscription/")

    def create_your_account(self):
        return self.page.get_by_role("heading", name="Create Your Account")
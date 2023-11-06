from abcmouse.base.base_page import BasePage


class SubscriptionPage(BasePage):
    def __init__(self, page, url):
        super().__init__(page, url)

    def create_your_account(self):
        return self.page.get_by_role("heading", name="Create Your Account")
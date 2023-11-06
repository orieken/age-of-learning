from abcmouse.base.base_page import BasePage


class RegistrationPage(BasePage):
    email_error_message_text = ("Error - Please enter a valid email address. "
                                "It is a required field and must be filled in.")

    def __init__(self, page):
        super().__init__(page)

    def navigate_to(self):
        self.page.goto("https://www.abcmouse.com/abc/prospect-register/")

    def become_a_member_message(self):
        return self.page.get_by_role("heading", name="Become a Member!")

    def email_address(self):
        return self.page.get_by_placeholder("Email Address")

    def submit(self):
        return self.page.get_by_role("button", name="Submit", exact=True)

    def email_error_message(self):
        return self.page.get_by_role("alert", name=self.email_error_message_text)


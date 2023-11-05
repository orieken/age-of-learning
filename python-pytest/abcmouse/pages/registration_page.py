from abcmouse.base.page import Page


class RegistrationPage(Page):
    def __init__(self, driver, url='https://www.abcmouse.com/abc/prospect-register/'):
        super().__init__(driver, url)

    def email(self):
        locator = [
            'return document.querySelector(\"body > route-view\")',
            '.shadowRoot.querySelector(\"#page-component\")',
            '.shadowRoot.querySelector(\"#email\")'
        ]
        return self.js_locator(locator)

    def email_error_message(self):
        locator = [
            'return document.querySelector(\"body > route-view\")',
            '.shadowRoot.querySelector(\"#page-component\")',
            '.shadowRoot.querySelector(\"#email-error-message\")'
        ]
        return self.js_locator(locator)

    def submit(self):
        locator = [
            'return document.querySelector(\"body > route-view\")',
            '.shadowRoot.querySelector(\"#page-component\")',
            '.shadowRoot.querySelector(\"#submit-button\")'
        ]
        return self.js_locator(locator)

    def register(self, email):
        self.email().send_keys(email)
        self.submit().click()

    def become_a_member_message(self):
        locator = [
            'document',
            '.querySelector("body > route-view")',
            '.shadowRoot.querySelector("#page-component")',
            '.shadowRoot.querySelector("#become-member")'
        ]
        return self.js_locator(locator)
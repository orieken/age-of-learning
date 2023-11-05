from abcmouse.base.page import Page


class LandingPage(Page):
    def __init__(self, driver):
        super().__init__(driver)

    def signup(self):
        locator = [
            'return document',
            '.querySelector(\"body > route-view\")',
            '.shadowRoot.querySelector(\"#page-component\")',
            '.shadowRoot.querySelector(\"main-layout > header > home-header '
            '> authstate-context:nth-child(3) > signup-button\")']
        return self.js_locator(locator)
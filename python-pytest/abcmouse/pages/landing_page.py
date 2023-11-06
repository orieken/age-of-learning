from abcmouse.base.page import Page


class LandingPage(Page):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    def signup(self):
        locator = [
            'document',
            '.querySelector(\"body > route-view\")',
            '.shadowRoot.querySelector(\"#page-component\")',
            '.shadowRoot.querySelector(\"main-layout > header > home-header '
            '> authstate-context:nth-child(3) > signup-button\")']
        return self.js_locator(locator)
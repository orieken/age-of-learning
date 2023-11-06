from abcmouse.base.page import Page


class SubscriptionPage(Page):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    def heading(self):
        locator = [
            'document',
            '.querySelector("body > route-view")',
            '.shadowRoot.querySelector("#page-component")',
            '.shadowRoot.querySelector("#subscription-form > h3")'
        ]
        return self.js_locator(locator)

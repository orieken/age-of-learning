from playwright.sync_api import Page, expect

from abcmouse.mouse import Mouse


def test_landing_page_signup_should_be_displayed(page: Page):
    abc_mouse = Mouse(page)
    landing_page = abc_mouse.landing_page
    landing_page.navigate_to()
    expect(landing_page.signup()).to_contain_text('Sign Up')
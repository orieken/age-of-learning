from playwright.sync_api import Page, expect

from abcmouse.factories.user_factory import UserFactory
from abcmouse.mouse import Mouse


def test_submit_with_no_email_displays_error_message(page: Page):
    abc_mouse = Mouse(page)
    landing_page = abc_mouse.landing_page
    landing_page.navigate_to()
    landing_page.signup().click()
    registration_page = abc_mouse.registration_page
    registration_page.submit().click()
    expect(registration_page.email_error_message()).to_contain_text('Please enter a valid email address.')


def test_can_register_a_user(page: Page):
    user_factory = UserFactory()
    user = user_factory.create_user()

    abc_mouse = Mouse(page)
    landing_page = abc_mouse.landing_page
    landing_page.navigate_to()
    landing_page.signup().click()
    registration_page = abc_mouse.registration_page
    registration_page.register(user.email)
    subscription_page = abc_mouse.subscription_page
    expect(subscription_page.heading()).to_contain_text('Create Your Account')


def test_become_a_member_message_is_displayed(page: Page):
    abc_mouse = Mouse(page)
    registration_page = abc_mouse.registration_page
    registration_page.navigate_to()
    expect(registration_page.become_a_member_message()).to_contain_text('Become a Member')

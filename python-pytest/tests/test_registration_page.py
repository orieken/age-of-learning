from abcmouse.factories.user_factory import UserFactory
from abcmouse.mouse import Mouse



def test_submit_with_no_email_displays_error_message(browser):
    abcmouse = Mouse(browser, "https://www.abcmouse.com/")
    abcmouse.navigate_to()
    landing_page = abcmouse.landing_page
    landing_page.wait(5)
    landing_page.signup().click()
    landing_page.wait(5)
    registration_page = abcmouse.registration_page
    registration_page.wait(5)
    registration_page.submit().click()
    assert registration_page.email_error_message().text == 'Please enter a valid email address.'


def test_can_register_a_user(browser):
    user_factory = UserFactory()
    user = user_factory.create_user()
    abcmouse = Mouse(browser, "https://www.abcmouse.com/")
    abcmouse.navigate_to()
    landing_page = abcmouse.landing_page
    landing_page.wait(5)
    landing_page.signup().click()
    landing_page.wait(5)
    registration_page = abcmouse.registration_page
    registration_page.wait(5)
    registration_page.register(user.email)
    registration_page.wait(5)
    subscription_page = abcmouse.subscription_page
    assert subscription_page.heading().text == 'Create Your Account'


def test_become_a_member_message_is_displayed(browser):
    abmouse = Mouse(browser, "https://www.abcmouse.com/")
    registration_page = abmouse.registration_page
    registration_page.navigate_to()
    registration_page.wait(5)
    assert registration_page.become_a_member_message().text == 'Become a Member!'

from abcmouse.mouse import Mouse


def test_landing_page_signup_should_be_displayed(browser):
    abcmouse = Mouse(browser)
    # // wait for the page to load
    abcmouse.navigate_to()
    # // wait for 3 seconds
    landing_page = abcmouse.landing_page
    landing_page.wait(3)
    # print out the text of the signup button
    print(landing_page.signup().text)
    assert landing_page.signup().text == "Sign Up"

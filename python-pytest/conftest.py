import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    # Initialize the WebDriver (assuming you've downloaded and set up ChromeDriver)
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
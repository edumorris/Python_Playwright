import time
import os
import pytest

from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="module")
def the_internet_setup(browser_setup):
    page = browser_setup
    page.goto(os.environ["internet_url"])

    return page

def test_the_internet(the_internet_setup):
    page = the_internet_setup

    h1_element = page.locator(".heading")

    assert page.locator(".heading").inner_text() == "Welcome to the-internet"

    time.sleep(3)

def test_xpath_click(browser_setup):
    page = browser_setup
    page.locator("//a[contains(@href, '/abtest')]").click()
    time.sleep(3)
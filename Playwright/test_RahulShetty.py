import time
import os
import pytest
from playwright.sync_api import Page, expect

from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="module")
def rahul_shetty_setup(browser_setup):
    page = browser_setup
    page.goto(os.environ["rahul_shetty_url"])
    return page

def test_login(rahul_shetty_setup):
    page = rahul_shetty_setup

    # Enter username
    page.locator("#username").fill(os.environ["rs_login_uname"])
    # Enter password
    page.locator("#password").fill(os.environ["rs_login_pwd"])
    # Select user type
    page.locator("//input[@id='usertype' and @value='admin']").click()
    # page.locator("#userType[@value, 'user']").click()
    page.locator("//select[@class='form-control']").select_option("teach")
    # Agree to terms and conditions
    page.locator("//input[@id='terms']").click()
    # Sign in
    page.locator("#signInBtn").click()

    expect(page.locator("//h1[@class='my-4']")).to_be_visible()
    assert page.locator("//h1[@class='my-4']").inner_text() == "Shop Name"

    time.sleep(5)

def test_wrong_login(rahul_shetty_setup):
    page = rahul_shetty_setup

    # Enter username
    page.locator("#username").fill(os.environ["rs_login_uname"])
    # Enter password
    page.locator("#password").fill("wrong_password")
    # Select user type
    page.locator("//select[@class='form-control']").select_option("teach")
    # Agree to terms and conditions
    page.locator("//input[@id='terms']").click()
    # Sign in
    page.locator("#signInBtn").click()

    expect(page.locator(".alert-danger")).to_be_visible()

    time.sleep(5)

import re
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

@pytest.fixture(scope="function")
def page_login(rahul_shetty_setup):
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


def test_login(rahul_shetty_setup, page_login):
    page = rahul_shetty_setup

    expect(page.locator("//h1[@class='my-4']")).to_be_visible()
    assert page.locator("//h1[@class='my-4']").inner_text() == "Shop Name"

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

def test_add_items_to_cart(rahul_shetty_setup, page_login):
    page = rahul_shetty_setup

    # Select products
    productA = page.locator("app-card").filter(has_text=os.environ["productA"])
    productA.get_by_role("button").click()

    productB = page.locator("app-card").filter(has_text=os.environ["productB"])
    productB.get_by_role("button").click()

    # Checkout
    page.get_by_text("Checkout").click()

    # ToDo: add test to validate products
    products = page.locator("//h4[@class='media-heading']/a")


    expect(page.locator(".media-body")).to_have_count(2)

def test_new_tab(rahul_shetty_setup):
    page = rahul_shetty_setup

    # Handling a page opened in another tab
    with page.expect_popup() as new_page:
        page.locator("//a[@class='blinkingText' and @href='https://rahulshettyacademy.com/documents-request' ]").click()
        child_page = new_page.value
        expect(child_page.locator("//section[@class='page-title']//h1")).to_have_text("Documents request")
        # function .text_content() to get text

        text = child_page.locator(".red").text_content()


        email = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", text)

        print(email)

        assert email.__contains__("mentor@rahulshettyacademy.com")

    time.sleep(5)

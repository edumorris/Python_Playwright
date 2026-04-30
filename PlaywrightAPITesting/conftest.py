import pytest
import os
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="module")
def browser_setup(playwright):
    global browser

    if os.getenv("browser") == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif os.getenv("browser") == "firefox":
        browser = playwright.firefox.launch(headless=False)

    context = browser.new_context()
    page = context.new_page()
    return page
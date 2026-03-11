import pytest

# function will run for every test in the file.
# "module/class" will run once.
# "Session" will run once for whole execution
@pytest.fixture(scope="function")
def preWork():
    print("Setup  browser instance")

@pytest.fixture(scope="function")
def tearDown():
    yield
    print("teardown")

@pytest.fixture(scope="module")
def browser_setup(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://0.0.0.0:7080/")
    return page
from playwright.sync_api import Page

def test_playwright_basics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://0.0.0.0:7080/")

# chromium headless mode
def test_playwright_shortcut(page:Page):
    page.goto("http://0.0.0.0:7080/")




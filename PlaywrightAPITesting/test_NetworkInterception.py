import os
import time

from playwright.async_api import Playwright, expect
from playwright.sync_api import Page

from PlaywrightAPITesting.Utils.apiBase import APIUtils


def intercept_response(route):
    route.fulfill( # Full request with this data
        json = {
            'data': [],
            'message': 'No Orders'
        }
    )

def intercept_request(route):
    route.continue_(url=os.environ['client_shop_url'] + '/order/get-orders-details?id=69ca497ef86ba51a65361c23') # Continue request to server with this new URL


def test_network_intercept_with_fulfill(playwright: Playwright):
    page = playwright.chromium.launch(headless=False).new_context().new_page()
    page.goto(os.environ['client_api_url'])
    page.route(os.environ['client_shop_url'] + '/order/get-orders-for-customer/*', intercept_response)

    # Login
    page.get_by_placeholder('email@example.com').fill(os.environ['client_api_email'])
    page.get_by_placeholder('enter your passsword').fill(os.environ['client_api_pwd'])
    page.get_by_role('button', name='Login').click()
    page.get_by_role('button', name='ORDERS').click()

    # Add assertions

def test_network_intercept_unauthorised_route_continue(playwright: Playwright):
    page = playwright.chromium.launch(headless=False).new_context().new_page()
    page.route(os.environ['client_shop_url'] + '/order/get-orders-details?id=*', intercept_request)

    # Login
    page.goto(os.environ['client_api_url'])
    page.get_by_placeholder('email@example.com').fill(os.environ['client_api_email'])
    page.get_by_placeholder('enter your passsword').fill(os.environ['client_api_pwd'])
    page.get_by_role('button', name='Login').click()
    page.get_by_role('button', name='ORDERS').click()
    page.get_by_role('button', name='View').first.click()

    assert page.locator('.blink_me').text_content() == 'You are not authorize to view this order'
    # page.locator('//p[contains(concat(" ",  normalize-space(@class), " "), "blink_me")]')

def test_cookie_and_session_injection(playwright: Playwright):
    page = playwright.chromium.launch(headless=False).new_context().new_page()

    # Get token
    api_utils = APIUtils()
    user_token = api_utils.getToken(playwright)

    # Script to inject session in local storage
    page.add_init_script(f"""
        localStorage.setItem('token', '{user_token}')
    """)

    page.goto(os.environ['client_api_dashboard_url'])

    expect(page.locator('button').filter(has_text=' Sign Out ')).to_be_visible()
    # expect(page.get_by_role('button', name='ORDERS')).to_be_visible()

    time.sleep(3)

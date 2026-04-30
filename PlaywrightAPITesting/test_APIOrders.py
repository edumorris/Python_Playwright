import os
import time
import pytest
from playwright.sync_api import expect, Page, Playwright

from PlaywrightAPITesting.Utils.apiBase import APIUtils



def test_e2e_web_api(playwright: Playwright):
    page = playwright.chromium.launch(headless=False).new_context().new_page()

    page.goto(os.environ['client_api_url'])

    # Create order & get order id
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright)

    # Verify order
    page.get_by_placeholder('email@example.com').fill(os.environ['client_api_email'])
    page.get_by_placeholder('enter your passsword').fill(os.environ['client_api_pwd'])
    page.get_by_role('button', name='Login').click()

    # Verify order is placed in UI
    page.locator('//button[@routerlink="/dashboard/myorders"]').click()

    page.wait_for_selector('//tbody')
    orders = page.query_selector_all('//tbody/tr/th')

    index = 1

    # for order in orders:
    #     if orderId == order.text_content():
    #         break
    #     index += 1
    #
    # # print(index)
    # # print(orderId)
    #
    # order_element = page.locator(f'//tbody/tr[{index}]')

    order_element = page.locator('tr').filter(has_text=orderId)

    order_element.get_by_role('button', name='View').click()

    print("orderId : " + page.locator('//div[contains(concat(" ",normalize-space(@class)," ")," col-text")]').text_content())

    expect(page.locator('//p[@class="tagline"]')).to_be_visible()
    page.wait_for_selector("//small")
    # expect(page.locator('//div[contains(concat(" ",normalize-space(@class)," ")," col-text")]').text_content()).to_have_text(orderId) # ToDO: assert orderId on order view page

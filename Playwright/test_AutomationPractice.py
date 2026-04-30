import os
import time
import pytest
from playwright.sync_api import expect, Page


@pytest.fixture(scope="module")
def automation_practice_setup(browser_setup):
    page = browser_setup
    page.goto(os.environ["automation_practice_url"])
    return page

def test_ui_checks(automation_practice_setup):
    page = automation_practice_setup

    elm = page.get_by_placeholder("Hide/Show Example")

    expect(elm).to_be_visible()

    page.locator("#hide-textbox").click()

    expect(elm).to_be_hidden()

def test_popups(automation_practice_setup):
    page = automation_practice_setup

    # Alerts
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role('button', name='Confirm').click()

def test_iframes(automation_practice_setup):
    page = automation_practice_setup

    # Handling iFrames
    course_iframe = page.frame_locator('#courses-iframe')

    # Click element in iFrame
    course_iframe.get_by_role('link', name='All Access plan').click()
    txt = course_iframe.locator('//div[@class="text"]/h2').text_content()
    assert "Happy Subscibers" in txt

def test_check_table_data(automation_practice_setup):
    page = automation_practice_setup
    page.goto("https://rahulshettyacademy.com/seleniumPractise/")

    with page.expect_popup() as new_page:
        page.locator('//a[@href="#/offers"]').click()

        # price_col_val = 0

        # for index in range(page.locator("th").count()):
        #     if page.locator().nth(index).filter(has_text='Price').count() > 0: # ToDO: Issue getting element & looping
        #         price_col_val = index
        #         print(price_col_val)
        #         break

        # price_col_val = page.locator("th").filter(has_text='Price')
        rice_row = page.query_selector_all('//table/tbody/tr')

        for row in rice_row:
            column = row.query_selector_all('td')

            for col in column:
                print(col.text_content())

        # expect(rice_row.locator('td').nth(price_col_val)).to_have_text('37')



        time.sleep(3)

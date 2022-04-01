import time

from playwright.sync_api import Playwright, sync_playwright

from pom.xcontact_us_page import ContactUsPage

def test_submit_form(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    contact_us = ContactUsPage(page)
    contact_us.navigate()
    contact_us.submit_form("Leo", "Evergreen ave 555", "leo@email.com", "11-222-3333", "test subject", "message test")

with sync_playwright() as playwright:
    test_submit_form(playwright)
    time.sleep(5)
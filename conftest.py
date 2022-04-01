import pytest
import time
from playwright.sync_api import Playwright


@pytest.fixture(scope="function")
def set_up(browser):
    # Assess - Given
    # browser = playwright.chromium.launch(headless=False)      #, slow_mo=500)
    context = browser.new_context()
    # # Open new page
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    yield page
    page.close()


@pytest.fixture(scope="function")
def login_set_up(set_up):
    # Assess - Given
    # browser = playwright.chromium.launch(headless=False)      #, slow_mo=500)
    # context = browser.new_context()
    # # Open new page
    # page = context.new_page()

    page = set_up

    login_element_issue = True
    while login_element_issue:
        if not page.is_visible("[data-testid=\"signUp\\.switchToSignUp\"]"):
            page.click("'Log In'", timeout=2000)
        else:
            login_element_issue = False
        time.sleep(0.1)

    page.click("[data-testid=\"signUp\\.switchToSignUp\"]", timeout=2000)
    page.click("[data-testid=\"switchToEmailLink\"] >> [data-testid=\"buttonElement\"]")
    page.click("#input_input_emailInput_SM_ROOT_COMP12")                                  #(":nth-match(input[type=email],1)")
    page.fill('#input_input_emailInput_SM_ROOT_COMP12', "symon.storozhenko@gmail.com")    #(":nth-match(input[type=email],1)", "symon.storozhenko@gmail.com")
    page.click('input:below(:text("Password"))')
    page.fill('input:below(:text("Password"))', "test123")
    page.click("[data-testid=\"submit\"] >> [data-testid=\"buttonElement\"]")

    yield page


@pytest.fixture
def go_to_new_collection_page(page):
    # Assess - Given
    # browser = playwright.chromium.launch(headless=False)      #, slow_mo=500)
    # context = browser.new_context()
    # # Open new page
    # page = context.new_page()
    page.goto("/new-collection")
    page.set_default_timeout(3000)

    yield page
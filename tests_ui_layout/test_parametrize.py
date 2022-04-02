import time

import pytest
from playwright.sync_api import Playwright, sync_playwright

@pytest.mark.parametrize("email", ["symon.storozhenko@gmail.com",
                                            pytest.param('fakeemail', marks=pytest.mark.xfail),
                                            pytest.param("symon.storozhenko@gmail", marks=pytest.mark.xfail)])
@pytest.mark.parametrize("passwrd", ["test123",
                                            pytest.param("fakepasswrd", marks=pytest.mark.xfail),
                                            "test123"])

def test_user_can_login(page,email, passwrd) -> None:
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    login_element_issue = True
    while login_element_issue:
        if not page.is_visible("[data-testid=\"signUp\\.switchToSignUp\"]"):
            page.click("'Log In'")
        else:
            login_element_issue = False
        time.sleep(0.1)

    page.click("[data-testid=\"signUp\\.switchToSignUp\"]", timeout=2000)
    page.click("[data-testid=\"switchToEmailLink\"] >> [data-testid=\"buttonElement\"]")
    page.click("#input_input_emailInput_SM_ROOT_COMP12")                                  #(":nth-match(input[type=email],1)")
    page.fill('#input_input_emailInput_SM_ROOT_COMP12', email)    #(":nth-match(input[type=email],1)", "symon.storozhenko@gmail.com")
    page.click('input:below(:text("Password"))')
    page.fill('input:below(:text("Password"))', passwrd)
    page.click("[data-testid=\"submit\"] >> [data-testid=\"buttonElement\"]")

    page.wait_for_load_state()
    page.expect_navigation(url="https://symonstorozhenko.wixsite.com/website-1",
                           wait_until="domcontentloaded",
                           timeout=5000)
    #page.wait_for_selector("._1qtDu") #("[aria-label=\"symon.storozhenko account menu\"]")
    assert page.is_visible("text=Log In")
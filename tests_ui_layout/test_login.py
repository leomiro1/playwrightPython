import time

from playwright.sync_api import Playwright, sync_playwright, expect
import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_logged_user_can_view_my_orders_menu(login_set_up) -> None:
    # Assess - Given
    page = login_set_up

    # Act - When/And
    page.click("._1qtDu") #("[aria-label='symon.storozhenko account menu']")

    #Assert - Then
    assert page.is_visible("text=My Orders")

    # Click text=My Orders
    # with page.expect_navigation(url="https://symonstorozhenko.wixsite.com/website-1/account/my-orders"):
    # with page.expect_navigation():
    #     page.click("text=My Orders")
    # ---------------------
    # context.close()
    # browser.close()


# with sync_playwright() as playwright:
#     test_login(playwright)
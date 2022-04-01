
from pom.home_page_elements import HomePage
from playwright.sync_api import Playwright, sync_playwright
import pytest

@pytest.mark.integration
def test_about_us_section_verbiage(login_set_up) -> None:
    # Assess - Given
    page = login_set_up

    assert page.is_visible(HomePage.celebrating_beauty_header)
    assert page.is_visible(HomePage.celebrating_beauty_body)

    # context.close()
    # browser.close()


# with sync_playwright() as playwright:
#     test_about_us_section_verbiage(playwright)

#@pytest.mark.skip(reason="not ready")
#@pytest.mark.xfail(reason="faketest should not be visible")
@pytest.mark.regression
def test_about_us_section_verbiage_2(login_set_up) -> None:
    # Assess - Given
    page = login_set_up

    assert page.is_visible("text=Shop")

    assert page.is_visible(HomePage.celebrating_beauty_header)
    assert page.is_visible(HomePage.celebrating_beauty_body)

    # context.close()
    # browser.close()
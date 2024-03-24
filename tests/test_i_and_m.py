import pytest
from playwright.sync_api import sync_playwright
import allure
from conftest import base_url
from pages.basepage import Basepage

@allure.title("Traverse The I&M Website")
@allure.description("This test traverses the I&M website and attempts to fill in a form")
@allure.tag("UI", "POSITIVE")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.timeout(300)
@pytest.mark.webtest
def test_i_and_m(page):
    base_page = Basepage(page)
    base_page.run_test()

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    test_i_and_m(page)
    browser.close()

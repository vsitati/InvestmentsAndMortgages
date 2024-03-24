from playwright.sync_api import Page, expect
from tests.conftest import base_url

class Basepage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_homepage(self):
        self.page.goto("https://www.imbankgroup.com/ke/")

        expect(self.page.locator("#page-wrap-in")).to_contain_text("Providing you with more than just banking...")

    def navigate_to_personal_banking(self):
        self.page.locator("#menu-item-12094").get_by_role("link", name="Personal").click()
        expect(self.page.locator("h1")).to_contain_text("Personal Banking with I&M")

    def navigate_to_business_page(self):
        self.page.locator("#menu-item-12095").get_by_role("link", name="Business", exact=True).click()
        expect(self.page.get_by_role("img", name="I&M Bank Kenya - Business")).to_be_visible()

    def navigate_to_diaspora_page(self):
        self.page.locator("#menu-item-12093").get_by_role("link", name="Diaspora").click()
        expect(self.page.get_by_label("Online Payments").get_by_role("figure").locator("div")).to_be_visible()

    def navigate_to_about_us_page(self):
        self.page.locator("#menu-item-12100").get_by_role("link", name="About Us").click()
        expect(self.page.get_by_role("img", name="Meeting our Customers’")).to_be_visible()

    def navigate_to_cards_page(self):
        self.page.locator("#menu-item-17313").get_by_role("link", name="Cards").click()
        expect(self.page.locator("h1")).to_contain_text("Explore more with I&M Cards!")
        self.page.get_by_role("link", name="Find out more  Credit Cards").click()
        expect(self.page.get_by_role("link", name="I&M Visa International Gold").nth(1)).to_be_visible()
        self.page.get_by_role("link", name="I&M Visa International Gold").nth(1).click()

    def fill_application_form(self):
        self.page.get_by_role("button", name="Terms and Conditions +").click()
        self.page.get_by_placeholder("Enter Your Name").click()
        self.page.get_by_placeholder("Enter Your Name").fill("Victor Sitati")
        self.page.get_by_placeholder("Enter Your Email Address").click()
        self.page.get_by_placeholder("Enter Your Email Address").fill("vsitati@gmail.com")
        self.page.get_by_placeholder("Enter Phone Number").click()
        self.page.get_by_placeholder("Enter Phone Number").fill("0720599572")
        self.page.get_by_label("Nearest Branch*").select_option("Sarit Centre")
        self.page.get_by_label("I am interested, please").check()
        self.page.get_by_placeholder("Enter your Comments").click()
        self.page.get_by_placeholder("Enter your Comments").fill("New card")
        self.page.get_by_label("I have read and understood").check()

    def run_test(self):
        self.navigate_to_homepage()
        self.navigate_to_personal_banking()
        self.navigate_to_business_page()
        self.navigate_to_diaspora_page()
        self.navigate_to_about_us_page()
        self.navigate_to_cards_page()
        self.fill_application_form()

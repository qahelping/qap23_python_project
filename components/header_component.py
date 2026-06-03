from playwright.sync_api import Page, expect

from core.base_page import BasePage


class HeaderComponent(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.header_container = page.locator('.header')
        self.back_btn = self.header_container.locator('.back-btn')
        self.logo_link = self.header_container.locator('[href="/automation-lab"]')

        self.brand_title = self.header_container.locator('.brand_title')
        self.brand_subtitle = self.header_container.locator('.brand-subtitle')

    def click_back_button(self):
        self.back_btn.click()

    def click_logo_link(self):
        self.logo_link.click()

    def verify_header_component_visible(self, title = None, subtitle = None) -> None:
        expect(self.header_container).to_be_visible()
        expect(self.back_btn).to_be_visible()
        expect(self.logo_link).to_be_visible()

        if title and subtitle:
            expect(self.brand_title).to_contain_text(title)
            expect(self.brand_subtitle).to_contain_text(subtitle)

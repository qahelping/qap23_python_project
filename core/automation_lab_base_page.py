from playwright.sync_api import Page, expect

from components.header_component import HeaderComponent
from core.base_page import BasePage


class AutomationLabBasePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.header = HeaderComponent(page)


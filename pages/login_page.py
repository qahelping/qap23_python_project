from playwright.sync_api import Page, expect

from core.automation_lab_base_page import AutomationLabBasePage
from core.base_page import BasePage


class LoginPage(AutomationLabBasePage):

    path = '/login'
    title = 'Task Management Board'

    def __init__(self, page: Page):
        super().__init__(page)

        self.login_input = page.locator('#id-input-login-email-input')
        self.password_input = page.locator('#id-input-login-password-input')
        self.login_button = page.locator('[data-qa="login-submit-button"]')

    def open(self) -> None:
        self.goto(self.path)

    def verify_login_page_opened(self) -> None:
        super().verify_page_opened(self.path, self.title)
        expect(self.login_input).to_be_visible()
        expect(self.password_input).to_be_visible()
        expect(self.login_button).to_be_visible()

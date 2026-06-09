# import pytest
# from playwright.sync_api import Page
#
# from pages.automation_lab_page import AutomationLabPage
# from pages.login_page import LoginPage
# from pages.savings_page import SavingsPage
#
#
# def test_open_savings_page_directly(page: Page):
#     savings_page = SavingsPage(page)
#     savings_page.open()
#
#
#     savings_page.verify_goal_page_opened()
#     savings_page.verify_empty_state()
#
#
#
# def test_open_savings_page_via_automation_lab(page: Page):
#     automation_lab_page = AutomationLabPage(page)
#     automation_lab_page.open()
#     automation_lab_page.verify_page_opened()
#
#     automation_lab_page.open_savings_page()
#
#     savings_page = SavingsPage(page)
#     savings_page.verify_goal_page_opened()
#     savings_page.verify_empty_state()
#
#
#
# def test_open_tms_login(page: Page):
#     login_page = LoginPage(page)
#     login_page.open()
#     login_page.verify_login_page_opened()

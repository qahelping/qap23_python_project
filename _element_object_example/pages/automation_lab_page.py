from playwright.sync_api import Page

from core.base_page import BasePage
from _element_object_example.element_base import ElementBase


class AutomationLabPage(BasePage):

    path = '/automation-lab'
    title = 'Task Management Board'

    def __init__(self, page: Page):
        super().__init__(page)

        self.hero_title = ElementBase.by_css(page, '.hero-title')
        self.section_title = ElementBase.by_role(
            page,
            'heading',
            name='Категории',
            exact=True,
        )
        self.savings_card = ElementBase.by_test_id(page, 'feature-card-savings')
        self.open_savings_link = self.savings_card.child(
            self.savings_card.locator.get_by_role('link', name='Открыть →'),
        )

    def open(self) -> None:
        self.goto(self.path)

    def verify_page_opened(self) -> None:
        super().verify_page_opened(self.path, self.title)
        self.hero_title.should_contain_text('Web Automation Torture Lab')
        self.section_title.should_be_visible()
        self.savings_card.should_be_visible()

    def open_savings_page(self) -> None:
        self.open_savings_link.click()

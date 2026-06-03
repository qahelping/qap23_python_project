from playwright.sync_api import Page

from core.base_page import BasePage
from _element_object_example.element_base import ElementBase


class SavingsPage(BasePage):

    path = '/automation-lab/savings'
    title = 'Task Management Board'

    def __init__(self, page: Page):
        super().__init__(page)

        self.goals_page = ElementBase.by_test_id(page, 'goals-page')
        self.page_title = ElementBase.by_css(page, '.savings-title')
        self.page_subtitle = ElementBase.by_css(page, '.savings-subtitle')
        self.create_goal_button = ElementBase.by_test_id(page, 'create-goal-button')
        self.empty_state = ElementBase.by_test_id(page, 'goals-empty-state')
        self.empty_state_title = ElementBase.by_css(page, '.savings-empty-title')
        self.empty_state_text = ElementBase.by_css(page, '.savings-empty-text')
        self.create_goal_cta = ElementBase.by_test_id(page, 'create-goal-cta')

    def open(self) -> None:
        self.goto(self.path)

    def verify_page_opened(self) -> None:
        super().verify_page_opened(self.path, self.title)
        self.goals_page.should_be_visible()

    def verify_empty_state(self) -> None:
        self.page_title.should_have_text('Мои цели')
        self.page_subtitle.should_contain_text('Копите на мечту по плану')
        self.create_goal_button.should_be_visible()
        self.create_goal_button.should_have_text('+ Создать цель')
        self.empty_state.should_be_visible()
        self.empty_state_title.should_have_text('Пока нет ни одной цели')
        self.empty_state_text.should_contain_text('Создайте первую цель')
        self.create_goal_cta.should_be_visible()
        self.create_goal_cta.should_have_text('Создать первую цель')

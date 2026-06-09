import pytest
from playwright.sync_api import Page, expect, BrowserContext
from selenium.webdriver.common.bidi.script import EvaluateResultException

from pages.automation_lab_page import AutomationLabPage
from pages.login_page import LoginPage
from pages.savings_page import SavingsPage
from pathlib import Path

BASE_URL = 'http://localhost:3000/automation-playground'

@pytest.mark.advanced1
def test_selector(page: Page):
    page.set_viewport_size({"width": 1064, "height": 1200})
    page.goto(BASE_URL + '/dropdowns')

    page.locator('id=country-select').select_option('Беларусь')

    page.locator('.custom-dropdown-button').click()
    page.get_by_text('Минск').click()

    text = page.locator('.practice-result-body').all_text_contents()
    assert text == ['Страна: БеларусьГород: МинскЯзык: не выбранНавыки: не выбраныПроект: не выбран']


@pytest.mark.advanced2
def test_alert(page: Page):
    page.set_viewport_size({"width": 1064, "height": 1200})
    page.goto('https://the-internet.herokuapp.com/javascript_alerts')

    with page.expect_event("dialog") as dialog_info:
        page.locator('[onclick="jsPrompt()"]').click()

    dialog = dialog_info.value
    print(dialog.message)
    print(dialog.type)

    breakpoint()

    dialog.accept()


@pytest.mark.advanced3
def test_frame(page: Page):
    page.set_viewport_size({"width": 1064, "height": 1200})
    page.goto('https://the-internet.herokuapp.com/iframe')

    frame = page.frame_locator('iframe[id="mce_0_ifr"]')
    text = frame.locator('#tinymce > p').text_content()
    assert text


@pytest.mark.advanced4
def test_window(page: Page, context: BrowserContext):
    page.set_viewport_size({"width": 1064, "height": 1200})
    page.goto('https://the-internet.herokuapp.com/windows')

    page.locator('[href="/windows/new"]').click()

    pages = context.pages

    context = page.context
    pages = context.pages

    pages[-1].bring_to_front()
    pages[-1].locator('text=New Window')
    pages[0].locator('text=New Window')
    pages[-1].close()

    new_page = context.new_page()
    new_page.goto('https://the-internet.herokuapp.com/')


@pytest.mark.advanced5
def test_window_try_to_find(page: Page, context: BrowserContext):
    page.set_viewport_size({"width": 1064, "height": 1200})
    page.goto('https://the-internet.herokuapp.com/windows')

    with context.expect_page() as new_page_info:
        page.locator('[href="/windows/new"]').click()

    new_page = new_page_info.value

    new_page.wait_for_load_state('load', timeout=30000)

    assert 'windows/new' in new_page.url
    expect(new_page).to_have_url()

@pytest.mark.advanced7
def test_upload_file(page: Page):
    page.set_viewport_size({"width": 1064, "height": 1200})
    page.goto('https://the-internet.herokuapp.com/upload')

    path = '/Users/elenayanushevskaya/QAP/qap23_python_project/test_data/file.png'
    page.locator('[id="file-upload"]').set_input_files(path)

    breakpoint()
    page.locator('[id="file-submit"]').click()

    expect(page.locator('[id="uploaded-files"]')).to_contain_text('file.png')


@pytest.mark.advanced8
def test_download_file(page: Page):
    page.set_viewport_size({"width": 1064, "height": 1200})
    page.goto('https://the-internet.herokuapp.com/download')


    with page.expect_download() as download_info:
        page.locator('[href="download/chromedriver.exe"]').click()

    download = download_info.value
    assert download.suggested_filename

    file_path = Path('test_data/download/') / download.suggested_filename
    download.save_as(file_path)

    assert file_path.is_file()


@pytest.mark.advanced9
def test_clicks(page: Page, domain):
    page.set_viewport_size({"width": 1064, "height": 1200})
    page.goto(f'http://{domain}/automation-playground/click-types')


    page.locator('[aria-label="Простой клик"]').click()

    page.locator('[aria-label="Двойной клик"]').click(click_count=2)
    page.locator('[aria-label="Двойной клик"]').dblclick()

    page.locator('[aria-label="Клавиша Enter"]').press('Enter')

    page.locator('[aria-label="ActionChains: Ctrl плюс клик"]').click(modifiers=['ControlOrMeta'])

    page.locator('[aria-label="Зона наведения и клика"]').hover()
    page.locator('[aria-label="Наведение и клик"]').click()

    page.locator('[aria-label="JavaScript click"]').click(force=True)
    page.locator('[aria-label="JavaScript click"]').evaluate("element => element.click()")


@pytest.mark.advanced10
def test_wait(page: Page, domain):
    page.set_viewport_size({"width": 1064, "height": 1200})
    page.goto(f'http://{domain}/automation-playground/click-types')

    breakpoint()
    page.locator('[aria-label="Простой клик2"]').wait_for(timeout=100000, state='detached')
    expect(page.locator('[aria-label="Простой клик2"]')).not_to_be_visible()





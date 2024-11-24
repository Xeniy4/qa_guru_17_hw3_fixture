
import pytest
from selene import browser, be, have
from selenium import webdriver


@pytest.fixture(scope="session")
def prepare_browser():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    browser.config.window_height = 900
    browser.config.window_width = 1400
    browser.open('https://google.com')
    browser.config.timeout = 20
    yield
    browser.quit()


def test_browser(prepare_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests'))
    browser.element('[name="q"]').clear()


def test_something(prepare_browser):
    browser.element('[name="q"]').should(be.blank).type('111abc22s34').press_enter()
    browser.element('[class="card-section"]').should(have.text('По запросу 111abc22s34 ничего не найдено.'))

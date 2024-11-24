
import pytest
from selene import browser, be, have
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    print("Браузер")
    yield
    print("Закрыть браузер")


@pytest.fixture(scope="session")
def prepare_browser():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    browser.open('https://google.com')
    browser.config.timeout = 20
    browser.config.window_height = 1000
    browser.config.window_width = 500
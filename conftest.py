
import pytest
from selene import browser
from selenium import webdriver

@pytest.fixture(scope="function")
def prepare_browser():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    browser.config.window_height = 900
    browser.config.window_width = 1400
    browser.config.timeout = 7
    browser.open('https://duckduckgo.com/')

    yield
    browser.quit()


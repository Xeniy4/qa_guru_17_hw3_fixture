
import pytest
from selene import browser, be, have
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("Браузер")
    yield
    print("Закрыть браузер")
    browser.quit()


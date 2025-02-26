from selene import browser, be, have


def test_browser(prepare_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element("section[data-testid='mainline']").should(have.text('yashaka/selene: User-oriented Web UI browser tests'))



def test_something(prepare_browser):
    browser.element('[name="q"]').type('adfa232323хв3eввтттт%#$%&').press_enter()
    browser.element("section[data-testid='mainline']").should(have.text('По запросу adfa232323хв3eввтттт%#$%& результаты не найдены.'))

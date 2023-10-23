import allure

from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

from tests.conftest import ios


@ios
def test_enter_email():
    with allure.step('Enter email'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Button")).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Input")).type('hello@browserstack.com').press_enter()

    with allure.step('Validate email entered'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Output")).should(have.text('hello@browserstack.com'))



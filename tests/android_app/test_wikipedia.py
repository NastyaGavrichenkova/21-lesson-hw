import allure

from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

from tests.conftest import android


@android
def test_search():

    with allure.step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('Appium')

    with allure.step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


@android
def test_search_and_open_article():

    with allure.step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('Appium')

    with allure.step('Open the first article on the screen'):
        browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).first.click()

    with allure.step('Verify content in the article'):
        results = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/view_wiki_error_text'))
        results.should(have.text('An error occurred'))

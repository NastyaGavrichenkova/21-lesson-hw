import pytest
import allure
import allure_commons
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium import webdriver
from selene import browser, support
import os
import dotenv

from tests import utils

from tests.config import AppConfig

# @pytest.mark.parametrize('device_family', ['android', 'ios'])
# @pytest.mark.parametrize('device, android_version', [
#     ('Google Pixel 3XL', '9.0'),
#     ('Samsung Galaxy S20', '10.0'),
#     ('Oppo A96', '11.0')],
#                          ids=['Google Pixel 3XL', 'Samsung Galaxy S20', 'Oppo A96']
#                          )
# @pytest.mark.parametrize('device, ios_version', [
#     ('iPhone 13', '15'),
#     ('iPhone 14 Pro Max', '16')],
#                          ids=['iPhone 13', 'iPhone 14 Pro Max']
#                          )
# def select_device(self, device_family):
#     if device_family == 'android':
#
#         return {
#             "platformVersion": self.android_system_version,
#             "deviceName": self.android_device
#         }


app_config = AppConfig(dotenv.load_dotenv())


@pytest.fixture(scope='function', autouse=True)
def mobile_management(request):
    platform = request.param
    if platform == 'android':
        options = UiAutomator2Options().load_capabilities({
            'app': app_config.android_app_url,

            **app_config.android_device_and_platform_version,

            'bstack:options': {
                'projectName': 'First Python project',
                'buildName': 'browserstack-android-build-1',
                'sessionName': 'BStack first_android_test',

                **app_config.bstack_creds
            }
        })

    elif request.param == 'ios':
        options = XCUITestOptions().load_capabilities({

            "app": app_config.ios_app_url,

            **app_config.ios_device_and_platform_version,

            "bstack:options": {
                "projectName": "First Python project",
                "buildName": "browserstack-ios-build-1",
                "sessionName": "BStack first_ios_test",

                **app_config.bstack_creds
            }
        })

    with allure.step('Init ap session'):
        browser.config.driver = webdriver.Remote(
            app_config.remote_url,
            options=options
        )

    browser.config.timeout = float(os.getenv('timeout', '10.0'))
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    utils.attach_screenshot(browser)
    utils.attach_page_source(browser)

    session_id = browser.driver.session_id

    with allure.step('Tear down app session'):
        browser.quit()

    utils.attach_bstack_video(session_id)


ios = pytest.mark.parametrize('mobile_management', ['ios'], indirect=True)
android = pytest.mark.parametrize('mobile_management', ['android'], indirect=True)

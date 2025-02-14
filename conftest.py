import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "HapeTesting"
    options.app = "C:\\Users\\akmal\\Downloads\\SiprusEdu SIT Debug v0.24.49 (1).apk"
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
    yield driver
    return driver
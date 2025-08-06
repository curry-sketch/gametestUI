import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
import yaml

@pytest.fixture(scope='session')
def driver():
    with open('config/device_config.yaml') as f:
        config = yaml.safe_load(f)

    options = UiAutomator2Options().load_capabilities(config['capabilities'])
    driver = webdriver.Remote(config['appium_server'], options=options)
    yield driver
    driver.quit()

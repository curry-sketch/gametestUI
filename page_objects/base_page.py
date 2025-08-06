from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url: str):
        self.driver.get(url)

    def find_element(self, *args):
        return self.wait.until(EC.presence_of_element_located(args))

    def click(self, *args):
        element = self.find_element(*args)
        element.click()

    def input_text(self, text: str, *args):
        element = self.find_element(*args)
        element.clear()
        element.send_keys(text)

    def save_screenshot(self, file_path: str):
        self.driver.save_screenshot(file_path)
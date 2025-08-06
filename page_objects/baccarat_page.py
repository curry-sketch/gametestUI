from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

class BaccaratPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://atmosphere.g32-prod.com/gameLobbyHome"

    def open_game(self):
        self.open(self.url)

    def take_screenshot(self, file_path: str):
        self.save_screenshot(file_path)

    def click_start_button(self):
        self.click(By.ID, "start-button")  # Replace with actual ID or locator
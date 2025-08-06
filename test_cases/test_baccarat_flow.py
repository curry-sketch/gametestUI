from page_objects.baccarat_page import BaccaratPage


def test_baccarat_flow(driver):
    page = BaccaratPage(driver)
    page.open_game()
    page.take_screenshot(".\\screenshot\\baccarat_game.png")
    page.click_start_button()
    page.take_screenshot(".\\screenshot\\baccarat_game_after_start.png")    
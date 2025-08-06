from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

options = UiAutomator2Options().load_capabilities({
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "deviceName": "d4bc9422",  # 你可以用 adb devices 看设备名
    "browserName": "Chrome",
    "chromedriverExecutable": ".\\chromedriver\\chromedriver.exe",  # 改成你的路径
    "noReset": True
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

driver.get("https://atmosphere.g32-prod.com/gameLobbyHome")
time.sleep(10)

driver.save_screenshot(".\\screenshot\\baccarat_game.png")
driver.quit()

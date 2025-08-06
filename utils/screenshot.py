from datetime import datetime

def save_screenshot(driver, name="screenshot"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"{name}_{timestamp}.png"
    driver.save_screenshot(path)
    return path

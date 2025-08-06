import allure
from utils.websocket_monitor import WebSocketMonitor

@allure.feature("百家乐游戏")
@allure.story("打开游戏页面")
def test_open_game(driver):
    driver.get("https://atmosphere.g32-prod.com/gameLobbyHome")
    driver.save_screenshot(".\\screenshot\\canvas_test.png")
    assert "百家乐" in driver.title or "Baccarat" in driver.title
@allure.feature("百家乐游戏")
@allure.story("WebSocket 监控")
def test_websocket_monitor(driver):
    monitor = WebSocketMonitor("wss://atmosphere.g32-prod.com/ws")
    monitor.start()
    try:
        # 这里可以添加一些操作来触发 WebSocket 消息
        driver.get("https://atmosphere.g32-prod.com/gameLobbyHome")
        assert monitor.is_connected()
        messages = monitor.get_messages()
        assert len(messages) > 0
    finally:
        monitor.stop()
        monitor.close()
        assert not monitor.is_connected(), "WebSocket 连接未正确关闭"
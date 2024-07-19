from pages.alerts import Alerts
import time


def test_alert(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    assert not alert_page.alert()

    alert_page.alertsButton.click()
    time.sleep(2)
    assert alert_page.alert()

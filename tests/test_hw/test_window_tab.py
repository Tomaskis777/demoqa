from pages.window_tab import WindowTab
import time


def test_window(browser):
    window_tab = WindowTab(browser)

    window_tab.visit()
    assert window_tab.home.get_text() == 'Home'
    time.sleep(2)
    assert window_tab.viewport.get_dom_attribute('href') == 'https://demoqa.com'
    time.sleep(2)
    window_tab.home.click()
    time.sleep(10)

    assert browser.title == 'DEMOQA'
    time.sleep(4)

from pages.slider import Slider
import time
from selenium.webdriver.common.keys import Keys


def test_slider_v1(browser):
    slider = Slider(browser)

    slider.visit()
    assert slider.slide.exist()
    assert slider.inp.exist()
    time.sleep(2)

    while not slider.slide.get_dom_attribute('value') == '50':
        slider.slide.send_keys(Keys.ARROW_RIGHT)
    time.sleep(4)

    assert slider.inp.get_dom_attribute('value') == '50'

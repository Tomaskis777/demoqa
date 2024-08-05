import pytest
import time
from pages.radio_but import Radio


# @pytest.mark.skipif(True, reason='просто пропуск')
def test_decor_1(browser):
    radio = Radio(browser)

    radio.visit()
    radio.yes.click_force()
    assert radio.text.get_text() == 'You have selected Yes'
    time.sleep(4)

    radio.impressive.click_force()
    assert radio.text.get_text() == 'You have selected Impressive'
    time.sleep(2)

    assert 'disabled' in radio.no.get_dom_attribute('class')
    time.sleep(2)

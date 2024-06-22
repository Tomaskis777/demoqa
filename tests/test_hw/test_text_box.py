from pages.text_box import TextBox
import time


def test_text_box_inf(browser):
    page_box = TextBox(browser)

    page_box.visit()
    page_box.full_name.send_keys('Mr. Full')
    page_box.btn_sub.click_force()
    assert page_box.full_name2.get_text() == 'Name:Mr. Full'
    page_box.full_name.clear()
    time.sleep(2)
    page_box.cur_address.send_keys('123321 Ulitsa')
    page_box.btn_sub.click_force()
    time.sleep(3)
    assert page_box.cur_address2.get_text() == 'Current Address :123321 Ulitsa'

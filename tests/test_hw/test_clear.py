# import time
#
# from pages.text_box import TextBox
#
#
# def test_clear(browser):
#     text_box = TextBox(browser)
#
#     text_box.visit()
#     text_box.name.send_keys('tester')
#     time.sleep(2)
#     text_box.name.clear()
#     time.sleep(2)
#     assert text_box.name.get_text() == ''

# from pages.modal_dialogs import ModalDialogs
# import time
#
#
# def test_modal_elements(browser):
#     modal_elements = ModalDialogs(browser)
#
#     modal_elements.visit()
#     assert modal_elements.btn_modal.check_count_elements(count=5)
#     time.sleep(2)
#
# def test_navigation_modal(browser):
#     navig_page = ModalDialogs(browser)
#
#     navig_page.visit()
#     time.sleep(3)
#     browser.refresh()
#     time.sleep(3)
#     navig_page.btn_navig.click()
#     time.sleep(2)
#     browser.back()
#     time.sleep(2)
#     browser.set_window_size(900, 400)
#     browser.forward()
#     time.sleep(2)
#     browser.back()
#     time.sleep(2)
#     assert navig_page.equal_url()
#     time.sleep(2)
#     assert browser.title == 'DEMOQA'
#     time.sleep(2)
#     browser.set_window_size(1000, 1000)
#     time.sleep(4)

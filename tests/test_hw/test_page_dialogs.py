# from pages.modal_dialogs import ModalDialogs
# import time
#
# def test_modal_elements(browser):
#     modal_elements = ModalDialogs(browser)
#
#     modal_elements.visit()
#     assert modal_elements.btn_modal.check_count_elements(count=5)
#
#
# def test_navigation_modal(browser):
#     navig_page = ModalDialogs(browser)
#
#     navig_page.visit()
#     assert navig_page.equal_url()
#     navig_page.btn_navig.click()
#     time.sleep(3)
#     browser.refresh()
#     browser.back()
#     browser.set_window_size(900, 400)
#     browser.forward()
#     time.sleep(2)
#     assert browser.title == 'DEMOQA'
#     browser.set_window_size(1000, 1000)
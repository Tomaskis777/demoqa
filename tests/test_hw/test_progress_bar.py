# import time
#
# from pages.progress_bar import ProgressBar
#
#
# def test_progress_bar(browser):
#     page = ProgressBar(browser)
#
#     page.visit()
#     time.sleep(2)
#
#     page.button.click()
#
#     while True:
#         if page.bar.get_dom_attribute('aria-valuenow') == '50':
#             page.button.click()
#             break
#
#     time.sleep(4)

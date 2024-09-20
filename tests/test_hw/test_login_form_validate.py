# from pages.form_page import FormPage
# import time
#
#
# def test_log_form(browser):
#     log_form = FormPage(browser)
#
#     log_form.visit()
#     assert log_form.login_forma.get_dom_attribute('placeholder') == 'First Name'
#     assert log_form.login_forma2.get_dom_attribute('placeholder') == 'Last Name'
#     assert log_form.login_forma3.get_dom_attribute('placeholder') == 'name@example.com'
#     assert log_form.login_forma3.get_dom_attribute('pattern') == '^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'
#     log_form.btn_submit.click_force()
#     time.sleep(2)
#     assert log_form.login_forma4.get_dom_attribute('class') == 'was-validated'
#     time.sleep(2)

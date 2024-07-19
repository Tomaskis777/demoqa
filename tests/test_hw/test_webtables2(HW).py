# from pages.tables import Tables
# import time
#
#
# def test_webtable(browser):
#     web_table = Tables(browser)
#
#     web_table.visit()
#     web_table.btn_add.click()
#     time.sleep(2)
#
#     web_table.btn_submit.click()
#     web_table.add_form.send_keys('Tom')
#     web_table.add_form2.send_keys('Pirk')
#     web_table.add_form3.send_keys('tomaskis@mail.ru')
#     web_table.add_form4.send_keys('15')
#     web_table.add_form5.send_keys('1500')
#     web_table.add_form6.send_keys('SDP')
#     time.sleep(2)
#     web_table.btn_submit.click()
#     time.sleep(6)
#     web_table.btn_edit.click()
#     time.sleep(3)
#     web_table.add_form.clear()
#     time.sleep(3)
#     web_table.add_form.send_keys('Dima')
#     time.sleep(3)
#     web_table.btn_submit.click()
#     time.sleep(4)
#     web_table.btn_delete.click()
#     time.sleep(4)
#
#
# def test_webtables(browser):
#     web_table = Tables(browser)
#
#     web_table.visit()
#     web_table.btn.click()
#     time.sleep(2)
#
#     web_table.btn_prev.click()
#     time.sleep(1)
#     web_table.btn_next.click()
#
#     web_table.btn_add.click()
#     web_table.add_form.send_keys('Tom')
#     web_table.add_form2.send_keys('Pirk')
#     web_table.add_form3.send_keys('tomaskis@mail.ru')
#     web_table.add_form4.send_keys('15')
#     web_table.add_form5.send_keys('1500')
#     web_table.add_form6.send_keys('SDP')
#     time.sleep(2)
#     web_table.btn_submit.click()
#     time.sleep(2)
#
#     web_table.btn_add.click()
#     web_table.add_form.send_keys('Petr')
#     web_table.add_form2.send_keys('Ivanov')
#     web_table.add_form3.send_keys('tom@mail.ru')
#     web_table.add_form4.send_keys('33')
#     web_table.add_form5.send_keys('30000')
#     web_table.add_form6.send_keys('ZGT')
#     time.sleep(2)
#     web_table.btn_submit.click()
#
#     web_table.btn_add.click()
#     web_table.add_form.send_keys('Dima ')
#     web_table.add_form2.send_keys('Suhow')
#     web_table.add_form3.send_keys('321@mail.ru')
#     web_table.add_form4.send_keys('35')
#     web_table.add_form5.send_keys('50000')
#     web_table.add_form6.send_keys('RUS')
#     time.sleep(2)
#     web_table.btn_submit.click()
#     time.sleep(4)
#
#     web_table.btn_next.click()
#     time.sleep(1)
#     web_table.btn_prev.click()
#     time.sleep(10)

from pages.tables import Tables
import time


def test_webtable(browser):
    web_table = Tables(browser)

    web_table.visit()
    web_table.btn_add.click()
    time.sleep(2)

    web_table.btn_submit.click()
    web_table.add_form.send_keys('Tom')
    web_table.add_form2.send_keys('Pirk')
    web_table.add_form3.send_keys('tomaskis@mail.ru')
    web_table.add_form4.send_keys('15')
    web_table.add_form5.send_keys('1500')
    web_table.add_form6.send_keys('SDP')
    time.sleep(2)
    web_table.btn_submit.click()
    time.sleep(6)
    web_table.btn_edit.click()
    time.sleep(3)
    web_table.add_form.clear()
    time.sleep(3)
    web_table.add_form.send_keys('Dima')
    time.sleep(3)
    web_table.btn_submit.click()
    time.sleep(4)
    web_table.btn_delete.click()
    time.sleep(4)

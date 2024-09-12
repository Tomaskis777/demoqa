from pages.accordion import Accordion
import time


# def test_visible_accord_elem(browser):
#     element_page = Accordion(browser)
#
#     element_page.visit()
#     assert element_page.acord_element.visible()


# def test_visible_accordion(browser):
#     element_page = Accordion(browser)
#
#     element_page.visit()
#     element_page.acord_btn.click()
#     time.sleep(2)
#     # assert element_page.acord_element.visible()
#     assert element_page.acord_btn.visible()

# def test_visible_accordion(browser):
#     element_page = Accordion(browser)
#
#     element_page.visit()
#     element_page.acord_btn.click()
#     time.sleep(2)
#     # assert element_page.acord_element.visible()
#     assert not element_page.acord_element.visible()
#
def test_visible_accordion_default(browser):
    element_page = Accordion(browser)

    element_page.visit()
    time.sleep(2)
    # assert element_page.ac_element1.visible()
    assert not element_page.ac_element1.visible()
    time.sleep(2)
    assert not element_page.ac_element2.visible()
    time.sleep(2)
    assert not element_page.ac_element3.visible()





#
# def test_visible_accordion_default1(browser):
#     element_page = Accordion(browser)
#
#     element_page.visit()
#     # assert element_page.ac_element2.visible()
#     assert not element_page.ac_element2.visible()
#
# def test_visible_accordion_default2(browser):
#     element_page = Accordion(browser)
#
#     element_page.visit()
#     # assert element_page.ac_element3.visible()
#     assert not element_page.ac_element3.visible()
#

from selenium.webdriver.common.by import By
from pages.demoqa import DemoQa
# import time



def test_check_icon(browser):
    # browser.get('https://demoqa.com/')
    icon = browser.find_element(By.CSS_SELECTOR, '#app > header > a')

    if icon is None:
        print('Не найден')
    else:
        print('Найден')

    # demo_qa_page = DemoQa(browser)
    # demo_qa_page.visit()
    # time.sleep(3)
    # demo_qa_page.click_on_the_icon()
    # time.sleep(3)
    # assert demo_qa_page.equal_url()
    # assert demo_qa_page.exist_icon()

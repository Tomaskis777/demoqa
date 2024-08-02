from pages.base_page import BasePage
from components.components import WebElement
from selenium.common.exceptions import NoSuchElementException


class DemoQa(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        self.icon = WebElement(driver, '#app > header > a')
        self.btn_elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')
        self.text = WebElement(driver, "#app > footer > span")
        self.h5 = WebElement(driver, '#app > div > div > div.home-body > div > div')

    def exist_icon(self):
        try:
            self.icon.find_element()
        except NoSuchElementException:
            return False
        return True

    # def get_text(self):
    #     if self.text.get_text() == str("© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."):
    #         return True
    #     else:
    #         return False
    #
    # def get_text1(self):
    #     if self.text1.get_text() == str("Please select an item from left to start practice."):
    #         return True
    #     else:
    #         return False

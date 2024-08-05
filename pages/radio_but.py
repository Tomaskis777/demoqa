from pages.base_page import BasePage
from components.components import WebElement
from selenium.common.exceptions import NoSuchElementException


class Radio(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/radio-button'
        super().__init__(driver, self.base_url)

        self.yes = WebElement(driver, '#yesRadio')
        self.text = WebElement(driver, 'div:nth-child(3) > p')
        self.impressive = WebElement(driver, '#impressiveRadio')
        self.no = WebElement(driver, 'div.custom-control.disabled.custom-radio.custom-control-inline')

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

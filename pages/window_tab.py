from pages.base_page import BasePage
from components.components import WebElement


class WindowTab(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/links'
        super().__init__(driver, self.base_url)
        self.viewport = WebElement(driver, '#simpleLink')

        self.home = WebElement(driver, '#simpleLink')
        self.home2 = WebElement(driver, '#linkWrapper > p:nth-child(3)')

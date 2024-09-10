from components.components import WebElement
from pages.base_page import BasePage


class SwagLabs(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://www.saucedemo.com/'
        super().__init__(driver, self.base_url)

        self.icon = WebElement(driver, '#root > div > div.login_logo')
        self.name = WebElement(driver, '#user-name')
        self.password = WebElement(driver, '#password')

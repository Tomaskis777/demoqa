from pages.base_page import BasePage
from components.components import WebElement


class Alerts(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts/'
        super().__init__(driver, self.base_url)

        self.alertsButton = WebElement(driver, '#alertButton')

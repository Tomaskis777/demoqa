from pages.base_page import BasePage
from components.components import WebElement


class ProgressBar(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/progress-bar'
        super().__init__(driver, self.base_url)
        self.viewport = WebElement(driver, '#simpleLink')

        self.button = WebElement(driver, '#startStopButton')
        self.bar = WebElement(driver, '#progressBar > div')

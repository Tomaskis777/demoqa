from pages.base_page import BasePage
from components.components import WebElement


class CheckModal(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.modal_button = WebElement(driver, '#showSmallModal')
        self.modal_button2 = WebElement(driver, '#closeSmallModal')
        self.modal_button3 = WebElement(driver, '#showLargeModal')
        self.modal_button4 = WebElement(driver, '#closeLargeModal')

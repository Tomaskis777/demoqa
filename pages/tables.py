from pages.base_page import BasePage
from components.components import WebElement


class Tables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables/'
        super().__init__(driver, self.base_url)

        self.no_data = WebElement(driver, 'div.rt-table')
        self.btn_delete_row = WebElement(driver, '#delete-record-1')
        self.btn_delete2_row = WebElement(driver, '#delete-record-2')
        self.btn_delete3_row = WebElement(driver, '#delete-record-3')

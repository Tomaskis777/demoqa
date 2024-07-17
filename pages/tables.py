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

        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.btn_submit = WebElement(driver, '#submit')
        self.add_form = WebElement(driver, '#firstName')
        self.add_form2 = WebElement(driver, '#lastName')
        self.add_form3 = WebElement(driver, '#userEmail')
        self.add_form4 = WebElement(driver, '#age')
        self.add_form5 = WebElement(driver, '#salary')
        self.add_form6 = WebElement(driver, '#department')
        self.btn_edit = WebElement(driver, '#edit-record-4')
        self.btn_delete = WebElement(driver, '#delete-record-4')

        self.btn = WebElement(driver, 'option:nth-child(1)')
        self.btn_prev = WebElement(driver, 'div.-previous > button')
        self.btn_next = WebElement(driver, 'div.-next > button')



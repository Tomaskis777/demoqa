from pages.base_page import BasePage
from components.components import WebElement


class Accordion(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.acord_element = WebElement(driver, '#section1Content > p')
        self.acord_btn = WebElement(driver, '#section1Heading')
        self.ac_element1 = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.ac_element2 = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.ac_element3 = WebElement(driver, '#section3Content > p')



from selenium.webdriver.common.by import By
import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://demoqa.com/'

    def visit(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator):
        time.sleep(3)
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def get_url(self):
        self.find_element(locator='#app > header > a').click()

    def equal_url(selfs):
        if selfs.get_url() == 'https://demoqa.com/'
            return True

        else:
            return  False
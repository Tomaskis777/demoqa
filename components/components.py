from selenium.webdriver.common.by import By

class WebElement:
    def __init__(self, drive, locator=''):
        self.driver = driver
        self.locator = locator

    def click(self):
        self.driver.find_element().click()

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

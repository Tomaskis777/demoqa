from pages.base_page import BasePage

class ElementsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)

    def equal_url(self):
        if self.get_url() == self.base_url:
            return True
        else:
            return False
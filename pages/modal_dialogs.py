from components.components import WebElement
from pages.base_page import BasePage

class ModalDialogs(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btn_small_modal = WebElement(driver, '#showSmallModal')
        self.btn_large_modal = WebElement(driver, '#showLargeModal')
        self.btn_close_sm = WebElement(driver, '#closeSmallModal')
        self.btn_close_lm = WebElement(driver, '#closeLargeModal')



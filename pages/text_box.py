from components.components import WebElement
from pages.base_page import BasePage

class TextBox(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.full_name = WebElement(driver, '#userName')
        self.current_address = WebElement(driver, '#currentAddress.form-control')
        self.btn_submit = WebElement(driver, '#submit')
        self.text_output_name = WebElement(driver, '#name.mb-1')
        self.text_output_current_address = WebElement(driver, '#currentAddress.mb-1')
from pages.base_page import BasePage
from components.components import WebElement


class Accordion(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.hidden_text_1 = WebElement(driver, '#section1Content > p')
        self.btn_first = WebElement(driver, '#section1Heading')
        self.hidden_text_2_1 = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.hidden_text_2_2 = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.hidden_text_3 = WebElement(driver, '#section3Content > p')

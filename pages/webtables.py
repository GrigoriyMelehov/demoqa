from components.components import WebElement
from pages.base_page import BasePage

class WebTables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.no_rows_found = WebElement(driver, 'div.rt-noData')
        self.pencil_4_row = WebElement(driver, 'div:nth-child(4) span[id*="edit"] path')
        self.basket_1_row = WebElement(driver, 'span[id*="delete"] path')
        self.basket_4_row = WebElement(driver, 'div:nth-child(4) span[id*="delete"] path')
        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.btn_submit = WebElement(driver, '#submit')
        self.btn_next = WebElement(driver, 'div.-next > button')
        self.btn_previous = WebElement(driver, 'div.-previous > button')
        self.input_number = WebElement(driver, 'input[type=number]')

        self.table_header_element = WebElement(driver, 'div[class*="rt-th rt-resizable"]')


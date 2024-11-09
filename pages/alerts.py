from pages.base_page import BasePage
from components.components import WebElement


class Alerts(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts'
        super().__init__(driver, self.base_url)

        self.btn_alert = WebElement(driver, '#alertButton')
        self.btn_confirm = WebElement(driver, '#confirmButton')
        self.confirm_results =WebElement(driver, '#confirmResult')
        self.btn_prompt = WebElement(driver, '#promtButton')
        self.prompt_results = WebElement(driver, '#promptResult')

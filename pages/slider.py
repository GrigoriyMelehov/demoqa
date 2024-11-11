from pages.base_page import BasePage
from components.components import WebElement


class Slider(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/slider'
        super().__init__(driver, self.base_url)

        self.input_element= WebElement(driver, '#sliderValue')
        self.slider_element = WebElement(driver,  'span > input')
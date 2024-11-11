import time
from pages.slider import Slider
from selenium.webdriver.common.keys import Keys

def test_check_slider(browser):
    page = Slider(browser)

    page.visit()
    time.sleep(2)

    assert page.input_element.exist()
    assert page.slider_element.exist()

    while not page.input_element.get_attribute('value') == '50':
        page.slider_element.send_keys(Keys.ARROW_RIGHT)


    assert page.input_element.get_attribute('value') == '50'
    time.sleep(2)
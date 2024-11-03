from pages.accordion import Accordion
import time


def test_visible_accordion(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()
    assert accordion_page.hidden_text_1.visible()
    accordion_page.btn_first.click()
    time.sleep(2)
    assert not accordion_page.hidden_text_1.visible()

def test_visible_accordion_default(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()
    assert not accordion_page.hidden_text_2_1.visible()
    assert not accordion_page.hidden_text_2_2.visible()
    assert not accordion_page.hidden_text_3.visible()






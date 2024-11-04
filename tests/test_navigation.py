from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
import time

def test_navigation(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)

    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()

    demo_qa_page.refresh()
    browser.refresh()
    browser.back()
    time.sleep(2)
    browser.forward()
    time.sleep(2)
    assert elements_page.equal_url()


from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
import time

def test_go_to_page_elements(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)
    demo_qa_page.visit()
    time.sleep(5)
    assert demo_qa_page.equal_url()
    time.sleep(5)
    demo_qa_page.btn_elements.click()
    time.sleep(5)
    assert elements_page.equal_url()


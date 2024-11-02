from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
import time

def test_check_text_elements(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)
    demo_qa_page.visit()
    time.sleep(5)
    assert demo_qa_page.footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
    time.sleep(5)
    demo_qa_page.btn_elements.click()
    time.sleep(5)
    assert elements_page.center_element.get_text() == 'Please select an item from left to start practice.'



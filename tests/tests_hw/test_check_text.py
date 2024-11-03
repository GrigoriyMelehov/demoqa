from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
import time

def test_check_text_demoqa_footer(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    time.sleep(5)
    assert demo_qa_page.footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'

def test_check_elements_pega_element(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)
    demo_qa_page.visit()
    time.sleep(5)
    demo_qa_page.btn_elements.click()
    time.sleep(5)
    assert elements_page.center_element.get_text() == 'Please select an item from left to start practice.'

def test_page_elements(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    assert elements_page.text_elements.get_text() == 'Please select an item from left to start practice.'
    time.sleep(5)
    assert elements_page.icon.exist()
    time.sleep(5)
    assert elements_page.btn_sidebar_first.exist()
    time.sleep(5)
    assert elements_page.btn_sidebar_first_textbox.exist()




from pages.demoqa import DemoQa
import time

def test_check_demoqa_size(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    browser.set_window_size(1000, 300)
    time.sleep(2)
    browser.set_window_size(1000, 1000)
    time.sleep(2)

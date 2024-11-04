from pages.modal_dialogs import ModalDialog
from pages.demoqa import DemoQa
import time

def test_modal_elements(browser):
    model_dialogs = ModalDialog(browser)
    model_dialogs.visit()
    assert model_dialogs.btn_elements.check_count_elements(5)

def test_navigation_modal(browser):
    model_dialogs = ModalDialog(browser)
    demo_qa = DemoQa(browser)

    model_dialogs.visit()
    time.sleep(3)
    browser.refresh()
    time.sleep(3)
    model_dialogs.icon.click()
    time.sleep(3)
    browser.back()
    time.sleep(3)
    browser.set_window_size(900, 400)
    time.sleep(3)
    browser.forward()
    assert demo_qa.equal_url()
    assert demo_qa.get_title() == 'DEMOQA'
    browser.set_window_size(1000, 1000)


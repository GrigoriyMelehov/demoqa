import time
from pages.alerts import Alerts

def test_check_alert(browser):
    alert_page = Alerts(browser)

    alert_page.visit()

    assert not alert_page.alert()

    alert_page.btn_alert.click()
    time.sleep(10)

    assert alert_page.alert()
    alert_page.alert().accept()

def test_check_alert_text(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    alert_page.btn_alert.click()
    time.sleep(3)

    assert alert_page.alert().text == 'You clicked a button'
    alert_page.alert().accept()
    assert not alert_page.alert()

def test_check_alert_timer(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    alert_page.btn_alert_timer.click()
    time.sleep(7)

    assert alert_page.alert()
    alert_page.alert().accept()
    assert not alert_page.alert()

def test_check_confirm(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    alert_page.btn_confirm.click()
    time.sleep(3)
    alert_page.alert().dismiss()
    assert alert_page.confirm_results.get_text() == 'You selected Cancel'

def test_check_prompt(browser):
    alert_page = Alerts(browser)
    name = 'Grinja'

    alert_page.visit()
    alert_page.btn_prompt.click()
    time.sleep(3)
    alert_page.alert().send_keys(name)
    time.sleep(3)
    alert_page.alert().accept()
    time.sleep(3)
    assert alert_page.prompt_results.get_text() == f'You entered {name}'






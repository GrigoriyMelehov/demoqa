import time
from pages.webtables import WebTables


def test_check_webtables_next_previous_btns(browser):
    web_tables_page = WebTables(browser)

    web_tables_page.visit()

    def add_row():
        web_tables_page.btn_add.click()
        web_tables_page.first_name.send_keys('ivan')
        web_tables_page.last_name.send_keys('ivanov')
        web_tables_page.user_email.send_keys('tttt@ttt.tt')
        web_tables_page.age.send_keys('99')
        web_tables_page.salary.send_keys('111')
        web_tables_page.department.send_keys('rrr')
        web_tables_page.btn_submit.click()

    for i in range(5):
        add_row()
        time.sleep(1)

    web_tables_page.btn_next.scroll_to_elements()
    browser.set_window_size(1500, 1000)

    assert web_tables_page.btn_previous.get_dom_attribute('disabled')
    assert web_tables_page.btn_next.get_dom_attribute('disabled')

    for i in range(3):
        add_row()
        time.sleep(1)

    assert not web_tables_page.btn_next.get_dom_attribute('disabled')

    web_tables_page.btn_next.click()
    time.sleep(2)

    assert web_tables_page.input_number.get_attribute('value') == '2'
    assert not web_tables_page.btn_previous.get_dom_attribute('disabled')

    web_tables_page.btn_previous.click()
    time.sleep(2)

    assert web_tables_page.input_number.get_attribute('value') == '1'
    browser.set_window_size(1000, 1000)




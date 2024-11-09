import time
from pages.webtables import WebTables


def test_webtables(browser):
    web_tables_page = WebTables(browser)

    web_tables_page.visit()
    web_tables_page.btn_add.click()
    time.sleep(2)
    web_tables_page.first_name.send_keys('ivan')
    web_tables_page.last_name.send_keys('ivanov')
    web_tables_page.user_email.send_keys('tttt@ttt.tt')
    web_tables_page.age.send_keys('99')
    web_tables_page.salary.send_keys('111')
    web_tables_page.department.send_keys('rrr')
    time.sleep(2)
    web_tables_page.btn_submit.click()
    time.sleep(5)
    web_tables_page.pencil_4_row.click()
    web_tables_page.first_name.clear()
    time.sleep(2)
    web_tables_page.first_name.send_keys('Petr')
    time.sleep(2)
    web_tables_page.btn_submit.click()
    time.sleep(5)
    web_tables_page.basket_4_row.click()
    time.sleep(5)

# def test_delete_last_row(browser):
#     web_tables_page = WebTables(browser)
#
#     web_tables_page.visit()
#     list = browser.find_elements('span[id*="delete"] path')
#     web_tables_page.list[len(list)-1].click()
#     time.sleep(5)


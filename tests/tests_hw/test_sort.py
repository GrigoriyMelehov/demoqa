import time
from pages.webtables import WebTables

def test_check_sort_table(browser):
    web_tables = WebTables(browser)
    web_tables.visit()

    for web_tables.element in web_tables.table_header_element.find_elements():
        web_tables.element.click()
        time.sleep(3)
        assert 'sort' in web_tables.element.get_attribute('class')
        time.sleep(3)



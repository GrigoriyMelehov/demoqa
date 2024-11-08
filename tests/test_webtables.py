import time
from pages.webtables import WebTables


def test_webtables(browser):
    web_tables_page = WebTables(browser)

    web_tables_page.visit()

    assert not web_tables_page.no_rows_found.exist()

    while web_tables_page.basket_1_row.exist():
        web_tables_page.basket_1_row.click()
        time.sleep(1)

    assert web_tables_page.no_rows_found.exist()


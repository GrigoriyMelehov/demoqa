from pages.elements_page import ElementsPage

def test_find_elements(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    assert elements_page.btns_firts_menu.check_count_elements(9)
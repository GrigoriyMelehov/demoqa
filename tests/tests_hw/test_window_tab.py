import time
from pages.links import Links

def test_check_click_home(browser):
    links_page =Links(browser)
    num = len(browser.window_handles)

    links_page.visit()

    assert links_page.link_home.exist()
    assert links_page.link_home.get_attribute('href') == 'https://demoqa.com/' #в стилях нет последнего слэша

    links_page.link_home.click()
    time.sleep(2)

    assert len(browser.window_handles) == num + 1
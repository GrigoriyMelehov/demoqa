import time
from pages.progress_bar import ProgressBar


def test_progress_bar(browser):
    pb_page = ProgressBar(browser)

    pb_page.visit()
    time.sleep(2)

    assert pb_page.progress_bar.exist()
    assert pb_page.btn.exist()

    pb_page.btn.click()
    print(pb_page.progress_bar.get_attribute("class"))

    while True:
        if pb_page.progress_bar.get_dom_attribute("aria-valuenow") == "50":
            pb_page.btn.click()
            print(pb_page.progress_bar.get_attribute("aria-valuenow"))

            break

    assert pb_page.progress_bar.get_dom_attribute('aria-valuenow') == '50'
    time.sleep(2)
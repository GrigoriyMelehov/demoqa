from pages.accordion import Accordion
from pages.alerts import Alerts
from pages.browser_tab import BrowserTab
from pages.demoqa import DemoQa
import pytest

# def test_check_title_demoqa(browser):
#     demo_qa_page = DemoQa(browser)
#     demo_qa_page.visit()
#     assert demo_qa_page.get_title() == 'DEMOQA'

@pytest.mark.parametrize("pages", [Accordion, Alerts, DemoQa, BrowserTab])
def test_check_title_pages(browser, pages):
    page = pages(browser)
    page.visit()
    assert page.get_title() == 'DEMOQA'
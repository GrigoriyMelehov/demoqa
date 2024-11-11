from pages.demoqa import DemoQa
import pytest

@pytest.mark.skip
def test_check_decor(browser):
    page = DemoQa(browser)
    page.visit()
    assert page.head_text.check_count_elements(6)

    for element in page.head_text.find_elements():
        assert element.text != ''




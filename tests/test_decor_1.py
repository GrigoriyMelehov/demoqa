import pytest

from pages.radio import Radio


@pytest.mark.skipif(True, reason='пропуск')
def test_check_radio_btns(browser):
    page = Radio(browser)

    page.visit()
    page.yes.click_force()
    assert page.text.get_text() == 'You have selected Yes'

    page.impressive.click_force()
    assert page.text.get_text() == 'You have selected Impressive'

    assert 'disabled' in page.no.get_attribute('class')


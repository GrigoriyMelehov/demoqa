import time

from pages.base_page import BasePage
from pages.modal_dialogs import ModalDialogs
import urllib.request

a = ModalDialogs(BasePage)

if urllib.request.urlopen(a.base_url).getcode() == 200:
    def test_check_modal(browser):
        md = ModalDialogs(browser)

        md.visit()
        md.btn_small_modal.click()
        time.sleep(3)
        md.btn_close_sm.click()
        time.sleep(3)
        md.btn_large_modal.click()
        time.sleep(3)
        md.btn_close_lm.click()
        time.sleep(3)
else:
    print('Cтраница недоступна!')

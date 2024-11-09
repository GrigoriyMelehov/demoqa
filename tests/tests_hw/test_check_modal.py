import time

from pages.modal_dialogs import ModalDialogs
import urllib.request

if urllib.request.urlopen('https://demoqa.com/modal-dialogs').getcode() == 201:
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

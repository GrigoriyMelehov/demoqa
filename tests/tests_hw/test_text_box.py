from pages.text_box import TextBox
import time

def test_check_text(browser):
    text_box = TextBox(browser)
    for_example_1 = 'Ivan'
    for_example_2 = 'Sweet home'

    text_box.visit()
    text_box.full_name.clear()
    text_box.current_address.clear()

    text_box.full_name.send_keys(for_example_1)
    text_box.current_address.send_keys(for_example_2)
    time.sleep(3)
    text_box.btn_submit.click_force()
    text_box.text_output_current_address.scroll_to_elements()
    time.sleep(3)

    assert text_box.text_output_name.get_text() == 'Name:' + for_example_1
    assert text_box.text_output_current_address.get_text() == 'Current Address :' + for_example_2


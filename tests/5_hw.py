from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

#поиск элементов
def find_elements():

    text_element_username = driver.find_element(By.CSS_SELECTOR, '#user-name')
    if text_element_username is None:
        print('элемент "поле Username" не найден')
    else:
        print('элемент "поле Username" найден!УРА!')

    text_element_password = driver.find_element(By.CSS_SELECTOR, '#password')
    if text_element_password is None:
        print('элемент "поле Password" не найден')
    else:
        print('элемент "поле Password" найден!УРА!')

    element_button = driver.find_element(By.CSS_SELECTOR, '#login-button') #кнопка называется "LOGIN"
    if element_button is None:
        print('элемент "кнопка LOGIN" не найден')
    else:
        print('элемент "кнопка LOGIN" найден!УРА!')

find_elements()
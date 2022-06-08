import os
import string

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    def fill_input_field_by_css_selector(browser_local, selector_str, send_keys_str, label_str=""):
        input_field_element = browser_local.find_element(By.CSS_SELECTOR, selector_str)
        # Check if label for that input field has correct text. Might not be included in THAT test-case, but might be useful to check if field looks like as required for the end-user
        # parent_element = input_field_element.find_element(By.XPATH,"..")
        # label_element = parent_element.find_element(By.CSS_SELECTOR, "label")
        # assert label_element.text == label_str
        input_field_element.send_keys(send_keys_str)


    fill_input_field_by_css_selector(browser,"input[name=\"firstname\"]", "Example first name")
    fill_input_field_by_css_selector(browser, "input[name=\"lastname\"]", "Example last name")
    fill_input_field_by_css_selector(browser, "input[name=\"email\"]", "Example email")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'requirements.txt')  # добавляем к этому пути имя файла
    browser.find_element(By.CSS_SELECTOR, "input#file").send_keys(file_path)




    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    # welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    # welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


def scroll_to_element(browser_local: webdriver.Chrome, selector_str: str):
    try:
        element = browser_local.find_element(By.CSS_SELECTOR, selector_str)
        browser_local.execute_script("return arguments[0].scrollIntoView(true);", element)
        return element
    finally:
        pass


try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x_element = scroll_to_element(browser, "span#input_value")
    x_value = int(x_element.text)

    scroll_to_element(browser, "input#answer").send_keys(calc(x_value))
    scroll_to_element(browser, "input#robotCheckbox").click()
    scroll_to_element(browser, "input#robotsRule").click()
    scroll_to_element(browser, "button[type=\"submit\"]").click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
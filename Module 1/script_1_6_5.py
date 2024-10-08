from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_link_text"
x = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.set_window_size(1920, 1080)
    browser.get(link)

    check_link = browser.find_element(By.PARTIAL_LINK_TEXT, x)
    check_link.click()

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Denis")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Sotnikov")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Moscow")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()
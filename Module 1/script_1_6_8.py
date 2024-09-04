from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.set_window_size(1920, 1080)
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "/html/body/div[1]/form/div[1]/input")
    input1.send_keys("Denis")
    input2 = browser.find_element(By.XPATH, "/html/body/div[1]/form/div[2]/input")
    input2.send_keys("Sotnikov")
    input3 = browser.find_element(By.XPATH, "/html/body/div[1]/form/div[3]/input")
    input3.send_keys("Moscow")
    input4 = browser.find_element(By.XPATH, "/html/body/div[1]/form/div[4]/input")
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, "/html/body/div[1]/form/div[6]/button[3]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
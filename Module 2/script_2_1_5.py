from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.set_window_size(1920, 1080)
browser.get(link)

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
time.sleep(0.5)

input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)
time.sleep(0.5)

input2 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
input2.click()
time.sleep(0.5)

input3 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
input3.click()
time.sleep(0.5)

input4 = browser.find_element(By.CLASS_NAME, "btn.btn-default")
input4.click()
time.sleep(10)
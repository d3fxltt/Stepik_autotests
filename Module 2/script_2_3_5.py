from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

#формула для расчета значения
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.set_window_size(1920, 1080)
browser.get(link)
time.sleep(0.7)

input1 = browser.find_element(By.CLASS_NAME, "trollface.btn.btn-primary")
input1.click()
time.sleep(0.7)

second_window = browser.window_handles[1]
browser.switch_to.window(second_window)

element1 = browser.find_element(By.ID, "input_value")
element1_text = element1.text
print(element1_text)
time.sleep(0.7)

calc_element1 = calc(element1_text)
print(calc_element1)
time.sleep(0.7)

element2 = browser.find_element(By.ID, "answer")
element2.send_keys(calc_element1)
time.sleep(0.7)

element3 = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
element3.click()
time.sleep(5)
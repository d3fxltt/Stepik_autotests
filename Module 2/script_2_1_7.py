from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

#формула для расчета значения
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

#заходим на сайт
link = "https://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.set_window_size(1920, 1080)
browser.get(link)
time.sleep(0.7)

#находим сундук и забираем числовое значение
treasure_open = browser.find_element(By.ID, "treasure")
x = treasure_open.get_attribute("valuex")
print(x)
time.sleep(0.7)

#считаем - это значения
y = calc(x)
print(y)
time.sleep(0.7)

#вводим туда значение
input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)
time.sleep(0.7)

#отмечает I'm the robot
input2 = browser.find_element(By.ID, "robotCheckbox")
input2.click()
time.sleep(0.7)

#отмечает Robots rule
input3 = browser.find_element(By.ID, "robotsRule")
input3.click()
time.sleep(0.7)

input4 = browser.find_element(By.CLASS_NAME, "btn.btn-default")
input4.click()
time.sleep(10)
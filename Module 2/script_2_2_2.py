from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

#формула для расчета значения
def calc(x, y):
  return str(int(x)+int(y))

link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.set_window_size(1920, 1080)
browser.get(link)
time.sleep(0.7)

#ищем элементы число1 и число2
sum_element1 = browser.find_element(By.ID, "num1")
sum1 = sum_element1.text
print(sum1)
time.sleep(0.7)

sum_element2 = browser.find_element(By.ID, "num2")
sum2 = sum_element2.text
print(sum2)
time.sleep(0.7)

z = calc(sum1, sum2)
print(z)
time.sleep(0.7)

select = Select(browser.find_element(By.CLASS_NAME, "custom-select"))
select.select_by_value(str(z))

submit = browser.find_element(By.CLASS_NAME, "btn.btn-default")
submit.click()
time.sleep(10)
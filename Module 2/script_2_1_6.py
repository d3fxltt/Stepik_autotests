from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)
browser.set_window_size(1920, 1080)

#находим элемент
people_radio = browser.find_element(By.ID, "peopleRule")

#находим атрибут прочекан
people_checked = people_radio.get_attribute("checked")

#проверяем, что с радиокнопкой
print("value of people radio: ", people_checked, "PASSED")

#находим элемент
robots_radio = browser.find_element(By.ID, "robotsRule")

#находим атрибут прочекан
robots_checked = robots_radio.get_attribute("checked")

print("value of robots radio: ", robots_checked, "PASSED")

#ассертим
assert robots_checked is None
assert people_checked is not None, "People radio is not selected by default"
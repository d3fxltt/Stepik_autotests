from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/simple_form_find_task.html"
    browser = webdriver.Chrome()
    browser.set_window_size(1920, 1080)
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()

# закрываем браузер после всех манипуляций
finally:
    browser.quit()
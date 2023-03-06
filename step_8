from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
# Формула

link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)
#Открываем браузер

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)



input_scroll = browser.find_element(By.TAG_NAME, "input")
browser.execute_script("return arguments[0].scrollIntoView(true);", input_scroll)
time.sleep(1)
#Скролим страницу до кнопки

input = browser.find_element(By.ID, "answer")
input.send_keys(y)
#Вставляем значение формулы


option1 = browser.find_element(By.ID, "robotCheckbox")
option1.click()


option2 = browser.find_element(By.ID, "robotsRule")
option2.click()

button = browser.find_element(By.TAG_NAME, "button")
button.click()

time.sleep(10)

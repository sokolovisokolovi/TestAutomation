from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
# Формула

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)
#Открываем браузер

option1 = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
option1.click()
#Нажимаем на кнопку


new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
#Переходим на новую вкладку

x_element = browser.find_element(By.XPATH, '//*[@id="input_value"]')
x = x_element.text
y = calc(x)
#Считываем число и присваиваем переменную для расчета в формуле

input = browser.find_element(By.CLASS_NAME, "form-control")
input.send_keys(y)
#Вставляем ответ из формулы

option1 = browser.find_element(By.XPATH, "/html/body/form/div/div/button")
option1.click()
#Нажимаем кнопку submit

time.sleep(10)

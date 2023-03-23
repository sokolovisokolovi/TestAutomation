from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
# Формула

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)
#Открываем браузер

option1 = browser.find_element(By.XPATH, '//*[@id="book"]')                         #Выбираем кнопку
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.XPATH, "//*[@id='price']"), "100"))    #Ставим ожидание до появления цены 100
option1.click()
#Нажимаем кнопку

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

time.sleep(5)

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
#Формула


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)
#Открываем браузер


x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)
#Выбираем число и присваиваем ему переменную

option3 = browser.find_element(By.XPATH, '//*[@id="answer"]')
option3.send_keys(y)
#Вставляем значение переменной в строку

option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
option1.click()
#Ставим чек-бокс

option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
option2.click()
#Выбраем radiobutton


button = browser.find_element(By.XPATH, '/html/body/div/form/button')
button.click()
#Нажимаем на кнопку Submit

time.sleep(10)

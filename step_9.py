from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
#Открываем браузер

input1 = browser.find_element(By.NAME, 'firstname')
input1.send_keys("Ivan")
input2 = browser.find_element(By.NAME, 'lastname')
input2.send_keys("Petrov")
input3 = browser.find_element(By.XPATH, '/html/body/div/form/div/input[3]')
input3.send_keys("test@mail.ru")
# Заполняем обязательные поля

input4 = browser.find_element(By.XPATH, '//*[@id="file"]')
#Выбираем кнопку прикрепить файл

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
element = browser.find_element(By.NAME, "file")
element.send_keys(file_path)
#Загружаем файл из папки


button = browser.find_element(By.TAG_NAME, "button")
button.click()
#Нажимаем кнопку sumbit

time.sleep(10)

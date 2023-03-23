from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
#формула


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)
#Открываем браузер и переходим по ссылке

x_element = browser.find_element(By.ID, "treasure")
x = x_element.get_attribute("valuex")
y = calc(x)

#Находим картинку


option3 = browser.find_element(By.XPATH, '//*[@id="answer"]')
option3.send_keys(y)


option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
option1.click()


option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
option2.click()

time.sleep(2)

button = browser.find_element(By.CSS_SELECTOR, '.btn-default')
button.click()

time.sleep(10)

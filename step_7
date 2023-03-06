from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select




link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)
#Открываем Браузер


n1 = browser.find_element(By.ID, "num1")
n2 = browser.find_element(By.ID, "num2")
#Присваиваем к переменным выведенные числа

x = n1.text
y = n2.text
s = int(x) + int(y)
#Складываем выведенные числа

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(str(s))
#Выбираем полученное число в открывшемся списке

button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
button.click()
#Нажимаем кнопку отправить

time.sleep(10)

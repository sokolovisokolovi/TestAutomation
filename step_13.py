import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.link = "http://suninjuly.github.io/registration2.html"

    def test_registration(self):
        browser = self.browser
        browser.get(self.link)

        # Заполняем обязательные поля
        input1 = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[1]/input')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[2]/input')
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[3]/input')
        input3.send_keys("test@mail.ru")
        input4 = browser.find_element(By.XPATH, '/html/body/div/form/div[2]/div[1]/input')
        input4.send_keys("12341234")
        input5 = browser.find_element(By.XPATH, '/html/body/div/form/div[2]/div[2]/input')
        input5.send_keys("street")

        # Отправляем заполненную форму
        button = browser.find_element(By.XPATH, '/html/body/div/form/button')
        button.click()

        
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_registration_wrong(self):
        browser = self.browser
        browser.get("http://suninjuly.github.io/registration1.html")

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[1]/input')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[2]/input')
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[3]/input')
        input3.send_keys("test@mail.ru")
        input4 = browser.find_element(By.XPATH, '/html/body/div/form/div[2]/div[1]/input')
        input4.send_keys("12341234")
        input5 = browser.find_element(By.XPATH, '/html/body/div/form/div[2]/div[2]/input')
        input5.send_keys("street")

        # Отправляем заполненную форму
        button = browser.find_element(By.XPATH, '/html/body/div/form/button')
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()

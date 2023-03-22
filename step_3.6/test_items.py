import pytest
from selenium.webdriver.common.by import By

def test_checking_the_button(browser):
    # переходим на страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # проверяем наличие кнопки "Добавить в корзину"
    add_to_cart_button = browser.find_element(By.XPATH, '//*[@id="add_to_basket_form"]/button')
    assert add_to_cart_button.is_displayed()
    

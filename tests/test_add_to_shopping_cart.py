# Импорт необходимых модулей из библиотеки Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pages.login_page import Login_page
# для применения явного ожидание
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
# Создаем класс для тестирования

def test_select_product():
    driver = webdriver.Chrome()
    print("Start test")
    login = Login_page(driver)
    login.autorization()
    # корзина
    shopping_cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@class="shopping_cart_link"]')))
    shopping_cart.click()
    print("Transition to cart")
    # header_product = WebDriverWait(driver, 30).until(
    #     EC.element_to_be_clickable(
    #         (By.XPATH, '//*[@class="inventory_item_name"]')))
    # value_header_product = header_product.text
    # assert value_header_product == "Sauce Labs Backpack"
    print("Successful Finish test")
    time.sleep(10)

# Импорт необходимых модулей из библиотеки Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from pages.cart_page import Cart_page
from pages.client_info_page import Client_info_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
# для применения явного ожидание
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

from pages.main_page import Main_page
from pages.payment_page import Payment_page

@pytest.mark.run(order=3)
def test_select_product_1(set_group):
    driver = webdriver.Chrome()
    print("Start test for product 1")
    login = Login_page(driver)
    login.autorization()
    mp = Main_page(driver)
    mp.select_product()
    cart_page = Cart_page(driver)
    cart_page.confirm_product()
    print("Successful finish test for product 1")

@pytest.mark.run(order=1)
def test_select_product_2():
    driver = webdriver.Chrome()
    print("Start test for product 2")
    login = Login_page(driver)
    login.autorization()
    mp = Main_page(driver)
    mp.select_product_2()
    cart_page = Cart_page(driver)
    cart_page.confirm_product()
    print("Successful finish test for product 2")

@pytest.mark.run(order=3)
def test_select_product_3():
    driver = webdriver.Chrome()
    print("Start test for product 3")
    login = Login_page(driver)
    login.autorization()
    mp = Main_page(driver)
    mp.select_product_3()
    cart_page = Cart_page(driver)
    cart_page.confirm_product()
    print("Successful finish test for product 3")

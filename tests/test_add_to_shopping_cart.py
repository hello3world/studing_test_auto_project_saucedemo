# Импорт необходимых модулей из библиотеки Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from pages.cart_page import Cart_page
from pages.client_info_page import Client_info_page
from pages.login_page import Login_page
# для применения явного ожидание
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

from pages.main_page import Main_page

def test_select_product():
    driver = webdriver.Chrome()
    print("Start test")
    login = Login_page(driver)
    login.autorization()
    mp = Main_page(driver)
    mp.select_product()
    cart_page = Cart_page(driver)
    cart_page.confirm_product()
    client_info_page = Client_info_page(driver)
    client_info_page.input_client_information()
    print("Successful finish test")
    time.sleep(10)

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


def test_link_about():
    driver = webdriver.Chrome()
    print("Start test")

    login = Login_page(driver)
    login.autorization()

    mp = Main_page(driver)
    mp.open_burger_menu_about()

    print("Successful finish test")

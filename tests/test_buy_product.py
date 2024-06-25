# Импорт необходимых модулей из библиотеки Selenium
from selenium import webdriver

import time

from pages.cart_page import Cart_page
from pages.client_info_page import Client_info_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page

from pages.main_page import Main_page
from pages.payment_page import Payment_page

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
    payment_page = Payment_page(driver)
    payment_page.payment()
    f = Finish_page(driver)
    f.screenshot_finish_page()
    print("Successful finish test")
    time.sleep(10)

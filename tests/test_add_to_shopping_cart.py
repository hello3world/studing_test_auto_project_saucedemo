# Импорт необходимых модулей из библиотеки Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
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
    print("Successful finish test")
    time.sleep(10)

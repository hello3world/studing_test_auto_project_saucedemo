# Импорт необходимых модулей из библиотеки Selenium
from selenium import webdriver
from pages.login_page import Login_page
from pages.main_page import Main_page

def test_link_about():
    driver = webdriver.Chrome()
    print("Start test")

    login = Login_page(driver)
    login.autorization()

    mp = Main_page(driver)
    mp.open_burger_menu_about()

    print("Successful finish test")

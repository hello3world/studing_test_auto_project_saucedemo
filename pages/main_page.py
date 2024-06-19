from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    btn_add_to_card_prod1 = '//button[@id="add-to-cart-sauce-labs-backpack"]'
    btn_add_to_card_prod2 = '//button[@id="add-to-cart-sauce-labs-bike-light"]'
    btn_add_to_card_prod3 = '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'
    card = '//a[@data-test="shopping-cart-link"]'
    btn_burger = '//button[@id="react-burger-menu-btn"]'
    btn_about = '//a[@data-test="about-sidebar-link"]'

    # Getters
    def get_btn_add_to_card_prd1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_add_to_card_prod1)))

    def get_btn_add_to_card_prd2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_add_to_card_prod2)))

    def get_btn_add_to_card_prd3(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_add_to_card_prod3)))

    def get_card(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.card)))

    def get_btn_burger(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_burger)))

    def get_btn_about(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_about)))

    # Actions
    def add_to_cart_product_1(self):
        self.get_btn_add_to_card_prd1().click()
        print("select product 1")

    def add_to_cart_product_2(self):
        self.get_btn_add_to_card_prd2().click()
        print("select product 2")

    def add_to_cart_product_3(self):
        self.get_btn_add_to_card_prd3().click()
        print("select product 3")

    def open_card(self):
        self.get_card().click()
        print("click by card")

    def open_burger_menu(self):
        self.get_btn_burger().click()
        print("open burger menu")

    def click_btn_about(self):
        self.get_btn_about().click()
        print("click button about")

    # Methods
    def select_product(self):
        self.get_current_url()
        self.add_to_cart_product_1()
        self.open_card()
        print("card is opened")

    def select_product_2(self):
        self.get_current_url()
        self.add_to_cart_product_2()
        self.open_card()
        print("card is opened")

    def select_product_3(self):
        self.get_current_url()
        self.add_to_cart_product_3()
        self.open_card()
        print("card is opened")


    def open_burger_menu_about(self):
        self.get_current_url()
        self.open_burger_menu()
        self.click_btn_about()
        self.assert_url("https://saucelabs.com/")
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
    card = '//a[@data-test="shopping-cart-link"]'

    # Getters
    def get_btn_add_to_card_prd1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_add_to_card_prod1)))

    def get_card(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.card)))

    # Actions
    def add_to_cart_product_1(self):
        self.get_btn_add_to_card_prd1().click()
        print("select product 1")

    def open_card(self):
        self.get_card().click()
        print("click by card")

    # Methods
    def select_product(self):
        self.get_current_url()
        self.add_to_cart_product_1()
        self.open_card()
        print("card is opened")

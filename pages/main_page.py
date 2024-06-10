from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    btn_add_to_card = '//button[@id="add-to-cart-sauce-labs-backpack"]'
    card = '//a[@data-test="shopping-cart-link"]'

    # Getters
    def get_btn_add_to_card(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_add_to_card)))

    def get_card(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.card)))

    # Actions
    def add_product_1(self):
        self.get_btn_add_to_card().click()
        print("choose product 1")

    def open_card(self):
        self.get_card().click()
        print("click by card")

    # Methods
    def select_product(self):
        self.get_current_url()
        self.add_product_1()
        self.open_card()
        print("card is opened")

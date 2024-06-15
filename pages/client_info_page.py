from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Client_info_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    first_name = '//input[@data-test="firstName"]'
    last_name = '//input[@data-test="lastName"]'
    zip_code = '//input[@data-test="postalCode"]'
    btn_continue = '//input[@data-test="continue"]'

    # Getters
    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_zip_code(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.zip_code)))

    def get_btn_continue(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_continue)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions
    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("input first name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("input last name")

    def input_zip_code(self, zip_code):
        self.get_zip_code().send_keys(zip_code)
        print("input zip code")


    def push_btn_continue(self):
        self.get_btn_continue().click()
        print("push button continue")

    # Methods
    def input_client_information(self):
        self.get_current_url()
        self.input_first_name("Yauheni")
        self.input_last_name("Paulovich")
        self.input_zip_code("220102")
        self.push_btn_continue()
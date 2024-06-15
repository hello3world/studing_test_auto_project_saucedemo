from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Payment_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    btn_finish = '//button[@data-test="finish"]'

    # Getters
    def get_btn_finish(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_finish)))

    # Actions
    def click_btn_finish(self):
        self.get_btn_finish().click()
        print("click btn finish")

    # Methods
    def payment(self):
        self.click_btn_finish()
        print("payment is finished")

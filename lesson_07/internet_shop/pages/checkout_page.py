from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")
        self.finish_button = (By.ID, "finish")
        self.complete_header = (By.CLASS_NAME, "complete-header")

    def fill_info(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.postal_code).send_keys(postal_code)
        return self

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()
        return self

    def get_total_price(self):
        return self.driver.find_element(*self.total_label).text

    def finish_checkout(self):
        self.driver.find_element(*self.finish_button).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.complete_header)
        )
        return self
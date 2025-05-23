from selenium.webdriver.common.by import By
from pages.checkout_page import CheckoutPage

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")
        self.cart_items = (By.CLASS_NAME, "inventory_item_name")

    def get_cart_items(self):
        return [item.text for item in self.driver.find_elements(*self.cart_items)]

    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()
        return CheckoutPage(self.driver)


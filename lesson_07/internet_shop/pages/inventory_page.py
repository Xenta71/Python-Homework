from selenium.webdriver.common.by import By
from pages.cart_page import CartPage

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def add_item_to_cart(self, item_name):
        item_xpath = f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"
        self.driver.find_element(By.XPATH, item_xpath).click()
        return self

    def get_cart_count(self):
        try:
            return int(self.driver.find_element(*self.cart_badge).text)
        except:
            return 0

    def go_to_cart(self):
        self.driver.find_element(*self.cart_link).click()
        return CartPage(self.driver)
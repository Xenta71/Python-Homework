from selenium.webdriver.common.by import By
from pages.inventory_page import InventoryPage

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open(self):
        self.driver.get(self.url)
        return self

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)
        return self

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)
        return self

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
        return InventoryPage(self.driver)  # Возвращаем следующий page object

    def login(self, username, password):
        self.open()
        self.enter_username(username)
        self.enter_password(password)
        return self.click_login()

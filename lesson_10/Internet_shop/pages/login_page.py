import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.inventory_page import InventoryPage


class LoginPage(BasePage):
    """Page Object для страницы авторизации."""

    def __init__(self, driver):
        """
        Инициализация страницы авторизации.

        :param driver: WebDriver - экземпляр Selenium WebDriver
        """
        super().__init__(driver)
        self.url = "https://www.saucedemo.com/"
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    @allure.step("Открыть страницу авторизации")
    def open(self) -> "LoginPage":
        """Открывает страницу авторизации.

        :return: LoginPage - экземпляр текущей страницы
        """
        self.driver.get(self.url)
        return self

    @allure.step("Ввести логин '{username}'")
    def enter_username(self, username: str) -> "LoginPage":
        """Вводит логин в соответствующее поле.

        :param username: str - логин пользователя
        :return: LoginPage - экземпляр текущей страницы
        """
        self._input(self.username_field, username)
        return self

    @allure.step("Ввести пароль")
    def enter_password(self, password: str) -> "LoginPage":
        """Вводит пароль в соответствующее поле.

        :param password: str - пароль пользователя
        :return: LoginPage - экземпляр текущей страницы
        """
        self._input(self.password_field, password)
        return self

    @allure.step("Нажать кнопку входа")
    def click_login(self) -> InventoryPage:
        """Нажимает кнопку входа в систему.

        :return: InventoryPage - экземпляр страницы инвентаря
        """
        self._click(self.login_button)
        return InventoryPage(self.driver)

    @allure.step("Выполнить вход с логином '{username}' и паролем")
    def login(self, username: str, password: str) -> InventoryPage:
        """Выполняет полный процесс авторизации.

        :param username: str - логин пользователя
        :param password: str - пароль пользователя
        :return: InventoryPage - экземпляр страницы инвентаря
        """
        return (
            self.open().enter_username(username).enter_password(password).click_login()
        )

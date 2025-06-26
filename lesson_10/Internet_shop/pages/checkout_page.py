from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
import allure


class CheckoutPage:
    """Page Object для страницы оформления заказа."""

    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы оформления заказа.

        Args:
            driver: WebDriver - экземпляр Selenium WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")
        self.finish_button = (By.ID, "finish")
        self.complete_header = (By.CLASS_NAME, "complete-header")

    @allure.step("Заполнение информации: {first_name} {last_name} {postal_code}")
    def fill_info(self, first_name: str, last_name: str, postal_code: str) -> 'CheckoutPage':
        """Заполняет информацию для оформления заказа.

        Args:
            first_name: Имя
            last_name: Фамилия
            postal_code: Почтовый индекс

        Returns:
            self для method chaining
        """
        self._fill_field(self.first_name, first_name)
        self._fill_field(self.last_name, last_name)
        self._fill_field(self.postal_code, postal_code)
        return self

    @allure.step("Нажатие кнопки Continue")
    def click_continue(self) -> 'CheckoutPage':
        """Нажимает кнопку продолжения оформления заказа.

        Returns:
            self для method chaining
        """
        self.driver.find_element(*self.continue_button).click()
        return self

    @allure.step("Получение итоговой суммы")
    def get_total_price(self) -> str:
        """Возвращает итоговую сумму заказа.

        Returns:
            Текст с итоговой суммой
        """
        return self.wait.until(
            EC.visibility_of_element_located(self.total_label)
        ).text

    @allure.step("Завершение оформления заказа")
    def finish_checkout(self) -> 'CheckoutPage':
        """Завершает оформление заказа.

        Returns:
            self после успешного завершения
        """
        self.driver.find_element(*self.finish_button).click()
        self.wait.until(
            EC.visibility_of_element_located(self.complete_header),
            message="Заголовок завершения не отобразился"
        )
        return self

    def _fill_field(self, locator: tuple, text: str) -> None:
        """Приватный метод для заполнения поля.

        Args:
            locator: Локатор поля
            text: Текст для ввода
        """
        element = self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Поле {locator} не найдено"
        )
        element.clear()
        element.send_keys(text)
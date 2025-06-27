from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    """Базовый класс для всех Page Object."""

    def __init__(self, driver: WebDriver):
        """
        Инициализация базовой страницы.

        Args:
            driver: Экземпляр WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step(f"Ввести текст '{text}' в элемент {locator}")
    def _input(self, locator: tuple, text: str) -> None:
        """Базовый метод для ввода текста.

        Args:
            locator: Кортеж (By, локатор)
            text: Текст для ввода
        """
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    @allure.step(f"Кликнуть по элементу {locator}")
    def _click(self, locator: tuple) -> None:
        """Базовый метод для клика по элементу.

        Args:
            locator: Кортеж (By, локатор)
        """
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step(f"Проверить видимость элемента {locator}")
    def _is_visible(self, locator: tuple) -> bool:
        """Проверяет видимость элемента.

        Args:
            locator: Кортеж (By, локатор)

        Returns:
            bool: True если элемент видим
        """
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

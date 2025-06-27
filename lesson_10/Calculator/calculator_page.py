from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure


class CalculatorPage:
    """Page Object для калькулятора с задержкой выполнения операций."""

    def __init__(self, driver):
        """
        Инициализация страницы калькулятора.

        :param driver: WebDriver - экземпляр Selenium WebDriver
        """
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_screen = (By.CSS_SELECTOR, ".screen")

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        """Открывает страницу калькулятора в браузере."""
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    @allure.step("Установить задержку выполнения операций в {seconds} секунд")
    def set_delay(self, seconds: int) -> None:
        """
        Устанавливает задержку выполнения операций.

        :param seconds: int - количество секунд задержки
        """
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    @allure.step(f"Нажать кнопку '{button_text}'")
    def click_button(self, button_text: str) -> None:
        """
        Нажимает кнопку калькулятора по тексту на кнопке.

        :param button_text: str - текст на кнопке (например, '7', '+', '=')
        """
        button_locator = (
            By.XPATH,
            f"//span[contains(@class, 'btn') and text()='{button_text}']",
        )
        self.driver.find_element(*button_locator).click()

    @allure.step("Получить результат вычисления")
    def get_result(self, timeout: int = 60) -> str:
        """
        Ожидает и возвращает результат вычисления.

        :param timeout: int - максимальное время ожидания в секундах (по умолчанию 60)
        :return: str - текст результата на экране калькулятора
        """
        WebDriverWait(self.driver, timeout).until(
            lambda d: "screen"
            in d.find_element(*self.result_screen).get_attribute("class")
            and d.find_element(*self.result_screen).text not in ["", "7+8"]
        )
        return self.driver.find_element(*self.result_screen).text

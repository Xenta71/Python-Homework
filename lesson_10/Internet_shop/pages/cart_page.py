from selenium.webdriver.common.by import By
import allure
from pages.base_page import BasePage
from pages.checkout_page import CheckoutPage


class CartPage(BasePage):
    """Page Object для страницы корзины."""

    def __init__(self, driver):
        super().__init__(driver)
        self.checkout_button = (By.ID, "checkout")
        self.cart_items = (By.CLASS_NAME, "inventory_item_name")

    @allure.step("Получить список товаров в корзине")
    def get_cart_items(self) -> list[str]:
        """Возвращает список названий товаров в корзине.

        Returns:
            list[str]: Список названий товаров
        """
        return [item.text for item in self.driver.find_elements(*self.cart_items)]

    @allure.step("Начать оформление заказа")
    def click_checkout(self) -> CheckoutPage:
        """Нажимает кнопку оформления заказа.

        Returns:
            CheckoutPage: Экземпляр страницы оформления заказа
        """
        self._click(self.checkout_button)
        return CheckoutPage(self.driver)

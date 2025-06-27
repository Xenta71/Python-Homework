from selenium.webdriver.common.by import By
import allure
from pages.base_page import BasePage
from pages.cart_page import CartPage


class InventoryPage(BasePage):
    """Page Object для страницы с товарами."""

    def __init__(self, driver):
        super().__init__(driver)
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    @allure.step(f"Добавить товар '{item_name}' в корзину")
    def add_item_to_cart(self, item_name: str) -> "InventoryPage":
        """Добавляет товар в корзину по названию.

        Args:
            item_name: Название товара

        Returns:
            InventoryPage: Экземпляр текущей страницы
        """
        item_xpath = (
            f"//div[text()='{item_name}']/"
            "ancestor::div[@class='inventory_item']//button"
        )
        self._click((By.XPATH, item_xpath))
        return self

    @allure.step("Получить количество товаров в корзине")
    def get_cart_count(self) -> int:
        """Возвращает текущее количество товаров в корзине.

        Returns:
            int: Количество товаров (0 если пусто)
        """
        try:
            return int(self.driver.find_element(*self.cart_badge).text)
        except Exception:
            return 0

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> CartPage:
        """Переходит на страницу корзины.

        Returns:
            CartPage: Экземпляр страницы корзины
        """
        self._click(self.cart_link)
        return CartPage(self.driver)

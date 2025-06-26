import sys
from pathlib import Path
import allure
import pytest

# Добавляем корень проекта в PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

from lesson_10.Internet_shop.pages.login_page import LoginPage
from lesson_10.Internet_shop.pages.inventory_page import InventoryPage
from lesson_10.Internet_shop.pages.cart_page import CartPage
from lesson_10.Internet_shop.pages.checkout_page import CheckoutPage


@allure.epic("SauceDemo Tests")
@allure.feature("Checkout Process")
class TestCheckout:
    @pytest.fixture(scope="function")
    def driver(self):
        """Фикстура для инициализации WebDriver"""
        with allure.step("Инициализация Firefox драйвера"):
            from selenium import webdriver
            options = webdriver.FirefoxOptions()
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")
            driver = webdriver.Firefox(options=options)
            driver.implicitly_wait(5)

        yield driver

        with allure.step("Завершение работы драйвера"):
            driver.quit()

    @allure.story("Проверка итоговой суммы заказа")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Проверка корректности расчета суммы заказа")
    @allure.description("""
    Тест проверяет корректность расчета общей суммы при добавлении 3 товаров:
    1. Авторизация стандартного пользователя
    2. Добавление товаров в корзину
    3. Оформление заказа
    4. Проверка итоговой суммы
    """)
    def test_checkout_total_amount(self, driver):
        test_items = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]
        user_data = ("standard_user", "secret_sauce")
        shipping_info = ("Xenia", "T", "603100")
        expected_total = "Total: $58.29"

        with allure.step("1. Авторизация пользователя"):
            allure.attach(
                f"Логин: {user_data[0]}\nПароль: {user_data[1]}",
                name="Учетные данные",
                attachment_type=allure.attachment_type.TEXT
            )
            inventory_page = LoginPage(driver).open().login(*user_data)

        with allure.step("2. Добавление товаров в корзину"):
            for item in test_items:
                inventory_page.add_item_to_cart(item)
                allure.attach(
                    item,
                    name="Добавленный товар",
                    attachment_type=allure.attachment_type.TEXT
                )

        with allure.step("3. Оформление заказа"):
            checkout_page = (
                inventory_page
                .go_to_cart()
                .click_checkout()
                .fill_info(*shipping_info)
                .click_continue()
            )
            allure.attach(
                f"Данные доставки:\nИмя: {shipping_info[0]}\nФамилия: {shipping_info[1]}\nИндекс: {shipping_info[2]}",
                name="Информация о доставке",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("4. Проверка итоговой суммы"):
            total = checkout_page.get_total_price()
            allure.attach(
                total,
                name="Итоговая сумма",
                attachment_type=allure.attachment_type.TEXT
            )

            assert expected_total in total, (
                f"Ожидаемая сумма: {expected_total}\n"
                f"Фактическая сумма: {total}"
            )
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from pages.inventory_page import InventoryPage

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_checkout_total_amount(driver):
    wait = WebDriverWait(driver, 5)

    inventory_page = LoginPage(driver).open().login("standard_user", "secret_sauce")
    wait.until(EC.url_contains("inventory"))

    for item in ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]:
        inventory_page.add_item_to_cart(item)

    checkout_page = inventory_page.go_to_cart().click_checkout()
    checkout_page.fill_info("Xenia", "T", "603100").click_continue()

    total = wait.until(lambda d: checkout_page.get_total_price())
    print(f"\nИтоговая сумма заказа - {total}")

    assert "Total: $58.29" in total

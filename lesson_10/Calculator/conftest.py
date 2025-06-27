import pytest
from selenium import webdriver
from calculator_page import CalculatorPage
import allure


@pytest.fixture
def driver():
    """Фикстура для инициализации и завершения работы WebDriver."""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def calculator(driver):
    """Фикстура для инициализации страницы калькулятора."""
    calc = CalculatorPage(driver)
    calc.open()
    return calc

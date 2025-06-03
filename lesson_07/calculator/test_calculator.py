import pytest
from selenium import webdriver
from calculator_page import CalculatorPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def calculator(driver):
    calc = CalculatorPage(driver)
    calc.open()
    return calc


def test_calculator_with_delay(calculator):
    calculator.set_delay(45)

    calculator.click_button("7")
    calculator.click_button("+")
    calculator.click_button("8")
    calculator.click_button("=")

    result = calculator.get_result()
    assert result == "15"

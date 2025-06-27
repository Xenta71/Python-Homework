import pytest
import allure
from calculator_page import CalculatorPage

@allure.feature("Тестирование калькулятора с задержкой")
@allure.severity(allure.severity_level.CRITICAL)
class TestCalculator:
    @allure.title("Проверка сложения с задержкой")
    @allure.description(
        "Тест проверяет операцию сложения с установленной задержкой выполнения"
    )
    def test_calculator_with_delay(self, calculator):
        with allure.step("Установить задержку выполнения операций"):
            calculator.set_delay(45)

        with allure.step("Выполнить операцию 7 + 8"):
            calculator.click_button("7")
            calculator.click_button("+")
            calculator.click_button("8")
            calculator.click_button("=")

        with allure.step("Проверить результат"):
            result = calculator.get_result()
            assert result == "15", f"Ожидался результат 15, получен {result}"

    @allure.title("Проверка различных операций")
    @allure.description("Параметризованный тест для проверки разных операций")
    @pytest.mark.parametrize(
        "a,op,b,expected",
        [(7, "+", 8, "15"), (9, "-", 3, "6"), (4, "*", 5, "20"), (8, "/", 2, "4")],
    )
    def test_calculator_operations(self, calculator, a, op, b, expected):
        with allure.step(f"Выполнить операцию {a} {op} {b}"):
            calculator.set_delay(2)
            calculator.click_button(str(a))
            calculator.click_button(op)
            calculator.click_button(str(b))
            calculator.click_button("=")

        with allure.step("Проверить результат"):
            result = calculator.get_result()
            assert (
                result == expected
            ), f"Ожидался результат {expected}, получен {result}"

# Проект тестирования калькулятора с PageObject и Allure

## Описание проекта
Проект содержит тесты для калькулятора с задержкой выполнения операций, реализованные с использованием:
- Selenium WebDriver
- Page Object Pattern
- Allure Framework

## Установка зависимостей
```bash
pip install -r requirements.txt
```

## Запуск тестов
1. Запуск тестов с генерацией Allure отчетов:
```bash
pytest --alluredir=allure-results lesson_10/test_calculator.py
```

2. Запуск Allure сервера для просмотра отчетов:
```bash
allure serve allure-results
```

## Просмотр отчетов
После выполнения тестов и запуска Allure сервера отчет будет автоматически открыт в браузере по умолчанию.

## Структура проекта
- `calculator_page.py` - Page Object для калькулятора
- `test_calculator.py` - тесты калькулятора
- `conftest.py` - фикстуры pytest

## Генерация отчета

Для генерации HTML-отчета выполните:
```bash
pytest --alluredir=allure-results -v 
```

Для просмотра отчета:
```bash
allure serve allure-results
```
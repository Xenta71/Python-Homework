# Тестовый проект SauceDemo

## Запуск тестов

1. Установите зависимости:
```bash
pip install -r requirements.txt
```

2. Запустите тесты с генерацией Allure-отчета:
```bash
pytest --alluredir=allure-results lesson_10/tests/
```

3. Сгенерируйте и откройте отчет:
```bash
allure serve allure-results
```

## Структура проекта

- `pages/` - Page Objects
- `tests/` - тесты
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

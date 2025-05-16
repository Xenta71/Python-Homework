import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.mark.usefixtures("driver")
def test_fill_form(driver):
    # Открытие страницы
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполнение формы
    fn = driver.find_element(By.NAME, "first-name")
    fn.send_keys("Иван")
    ln = driver.find_element(By.NAME, "last-name")
    ln.send_keys("Петров")
    address = driver.find_element(By.NAME, "address")
    address.send_keys("Ленина, 55-3")
    zip_code = driver.find_element(By.NAME, "zip-code")
    zip_code.send_keys("")
    city = driver.find_element(By.NAME, "city")
    city.send_keys("Москва")
    country = driver.find_element(By.NAME, "country")
    country.send_keys("Россия")
    e_mail = driver.find_element(By.NAME, "e-mail")
    e_mail.send_keys("test@skypro.com")
    ph_number = driver.find_element(By.NAME, "phone")
    ph_number.send_keys("+7985899998787")
    job_position = driver.find_element(By.NAME, "job-position")
    job_position.send_keys("QA")
    company = driver.find_element(By.NAME, "company")
    company.send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    zip_code_field = driver.find_element(By.ID, "zip-code").get_attribute("class")
    assert zip_code_field == "alert py-2 alert-danger"

    fields_to_check = ["#first-name", "#last-name", "#address", "#city", "#country", "#e-mail", "#phone", "#company"]

    for field in fields_to_check:
        field_class = driver.find_element(By.CSS_SELECTOR, field).get_attribute("class")
        assert field_class == "alert py-2 alert-success"

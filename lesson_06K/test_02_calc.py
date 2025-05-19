import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_slow_calculator():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    start_time = time.time()
    result = WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )
    end_time = time.time()

    elapsed_time = end_time - start_time
    assert 45 <= elapsed_time <= 50, f"Результат появился через {elapsed_time} секунд, ожидалось ~45 секунд"


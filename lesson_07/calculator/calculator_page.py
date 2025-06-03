from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_screen = (By.CSS_SELECTOR, ".screen")

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, seconds):
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    def click_button(self, button_text):
        button_locator = (By.XPATH, f"//span[contains(@class, 'btn') and text()='{button_text}']")
        self.driver.find_element(*button_locator).click()

    def get_result(self, timeout=60):
        WebDriverWait(self.driver, timeout).until(
            lambda d: "screen" in d.find_element(*self.result_screen).get_attribute("class") and
                      d.find_element(*self.result_screen).text not in ["", "7+8"]
        )
        return self.driver.find_element(*self.result_screen).text

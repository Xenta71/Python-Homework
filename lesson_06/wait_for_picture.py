from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")


WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR,"#image-container img:nth-child(4)"))
)

third_image = driver.find_element(By.CSS_SELECTOR,"#image-container img:nth-child(3)")
src_attribute = third_image.get_attribute("src")

print(src_attribute)

driver.quit()

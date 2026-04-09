from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    wait = WebDriverWait(driver, 10)
    zip_code = wait.until(EC.visibility_of_element_located((By.ID, "zip-code"))).get_attribute("class")
    assert "alert-danger" in zip_code
    first_name = wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).get_attribute("class")
    assert "alert-success" in first_name
    last_name = wait.until(EC.visibility_of_element_located((By.ID, "last-name"))).get_attribute("class")
    assert "alert-success" in last_name


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.NAME, "user-name").send_keys("standard_user")
    driver.find_element(By.NAME, "password").send_keys("secret_sauce")
    driver.find_element(By.NAME, "login-button").click()
    driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.NAME, "add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']").click()
    driver.find_element(By.NAME, "checkout").click()
    driver.find_element(By.NAME, "firstName").send_keys("Alla")
    driver.find_element(By.NAME, "lastName").send_keys("Mark")
    driver.find_element(By.NAME, "postalCode").send_keys("123456")
    driver.find_element(By.NAME, "continue").click()

    total = driver.find_element(By.XPATH, '//div[@class="summary_total_label"]').text
    print(f"{total}")

    driver.quit()

    total_sum = f"{total}"
    assert total_sum.strip() == "Total: $58.29"

    
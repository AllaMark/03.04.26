from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class Shop:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def auth(self):
        self.driver.find_element(By.NAME, "user-name").send_keys("standard_user")
        self.driver.find_element(By.NAME, "password").send_keys("secret_sauce")
        self.driver.find_element(By.NAME, "login-button").click()

    def add_cart(self):
        self.driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.NAME, "add-to-cart-sauce-labs-onesie").click()
        self.driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']").click()

    def checkout(self):
        self.driver.find_element(By.NAME, "checkout").click()

    def fill_form(self):
        self.driver.find_element(By.NAME, "firstName").send_keys("Alla")
        self.driver.find_element(By.NAME, "lastName").send_keys("Mark")
        self.driver.find_element(By.NAME, "postalCode").send_keys("123456")
        self.driver.find_element(By.NAME, "continue").click()

    def total(self):
        total = self.driver.find_element(By.XPATH, '//div[@class="summary_total_label"]').text
        return total

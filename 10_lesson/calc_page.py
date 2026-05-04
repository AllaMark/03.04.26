from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calc:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 46)

    def delay(self, num):
        self.driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(num)

    def button_click(self, symbol):
        self.driver.find_element(
            By.XPATH, f"//span[text()='{symbol}']"
        ).click()

    def result(self):
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.XPATH, '//div[@class="screen"]'), "15"
            )
        )
        res = self.driver.find_element(By.XPATH, '//div[@class="screen"]').text
        return res

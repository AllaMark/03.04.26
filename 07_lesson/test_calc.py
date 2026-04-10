import pytest
from selenium import webdriver
from calc_page import Calc

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver

    driver.quit()

def test_calc(driver):
    calc = Calc(driver)
    calc.delay("5")
    calc.button_click("7")
    calc.button_click("+")
    calc.button_click("8")
    calc.button_click("=")
    assert calc.result() == "15"
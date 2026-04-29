import pytest
import allure
from selenium import webdriver
from calc_page import Calc


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )
    yield driver
    driver.quit()


@allure.feature("Калькулятор")
@allure.story("Выполнение арифметических операций")
def test_calc(driver):
    calc = Calc(driver)

    with allure.step("Установить задержку 5 секунд"):
        calc.delay("5")

    with allure.step("Нажать кнопку '7'"):
        calc.button_click("7")

    with allure.step("Нажать кнопку '+'"):
        calc.button_click("+")

    with allure.step("Нажать кнопку '8'"):
        calc.button_click("8")

    with allure.step("Нажать кнопку '='"):
        calc.button_click("=")

    with allure.step("Проверить результат вычисления"):
        assert (
            calc.result() == "15"
        ), f"Ожидаемый результат: 15, фактический: {calc.result()}"

import pytest
import allure
from selenium import webdriver
from shop_page import Shop


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


@allure.feature("Интернет‑магазин")
@allure.story("Покупка товаров в интернет‑магазине")
@allure.severity(allure.severity_level.NORMAL)
def test_shop(driver):
    shop = Shop(driver)

    with allure.step("Выполнить авторизацию на сайте"):
        shop.auth()

    with allure.step("Добавить товары в корзину"):
        shop.add_cart()

    with allure.step("Перейти к оформлению заказа (checkout)"):
        shop.checkout()

    with allure.step("Заполнить форму доставки"):
        shop.fill_form()

    with allure.step("Проверить итоговую сумму заказа"):
        actual_total = shop.total().strip()
        expected_total = "Total: $58.29"
        assert (
            actual_total == expected_total
        ), f"Ошибка в итоговой сумме: ожидалось {expected_total}, получено {actual_total}"

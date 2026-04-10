import pytest
from selenium import webdriver
from shop_page import Shop

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver

    driver.quit()


def test_shop(driver):
#авторизация
    shop = Shop(driver)
    shop.auth()
#добавление товаров
    shop.add_cart()
#подтверждение
    shop.checkout()
#заполнить форму
    shop.fill_form()
#проверка 
    assert shop.total().strip() == "Total: $58.29"    


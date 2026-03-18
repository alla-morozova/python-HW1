import unittest
from selenium import webdriver
from login_page import LoginPage
from main_page import MainPage
from cart_page import CartPage
from checkout_page import CheckoutPage
from selenium.webdriver.firefox.service import Service
import allure


class TestShop(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        service = Service()
        cls.driver = webdriver.Firefox(service=service)
        cls.driver.get("https://www.saucedemo.com")

    @allure.feature("Покупка в интернет‑магазине")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title(
        "Полный сценарий покупки: авторизация,"
        " добавление товаров, оформление заказа")
    @allure.description(
        "Тест проверяет полный сценарий покупки: вход в аккаунт, "
        "добавление трёх товаров в корзину, переход к оформлению заказа, "
        "заполнение данных покупателя и проверку итоговой суммы."
    )
    def test_shop_functionality(self):
        login_page = LoginPage(self.driver)
        main_page = MainPage(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)

        with allure.step("Входим в аккаунт: вводим логин и пароль,"
                         " нажимаем кнопку входа"):
            login_page.enter_username("standard_user")
            login_page.enter_password("secret_sauce")
            login_page.click_login()

        with allure.step("Добавляем товары в корзину: рюкзак,"
                         " футболку и комбинезон"):
            main_page.add_backpack_to_cart()
            main_page.add_tshirt_to_cart()
            main_page.add_onesie_to_cart()

        with allure.step("Переходим в корзину и нажимаем Checkout"):
            main_page.go_to_cart()
            cart_page.click_checkout()

        with allure.step("Заполняем данные покупателя: имя,"
                         " фамилию и почтовый индекс"):
            checkout_page.fill_personal_info(
                "Алла", "Морозова", "032203"
            )

        with allure.step("Нажимаем кнопку Continue для перехода к оплате"):
            checkout_page.click_continue()

        with allure.step("Получаем итоговую сумму заказа"):
            total_price = checkout_page.get_total_price()

        with allure.step("Проверяем, что итоговая сумма равна $58.29"):
            assert total_price == "$58.29", \
                f"Expected $58.29, but got {total_price}"

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

import unittest
from selenium import webdriver
# from webdriver_manager.firefox import GeckoDriverManager
from login_page import LoginPage
from main_page import MainPage
from cart_page import CartPage
from checkout_page import CheckoutPage
from selenium.webdriver.firefox.service import Service


class TestShop(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        service = Service()
        cls.driver = webdriver.Firefox(service=service)
        cls.driver.get("https://www.saucedemo.com")

    def test_shop_functionality(self):
        login_page = LoginPage(self.driver)
        main_page = MainPage(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)

        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

        main_page.add_backpack_to_cart()
        main_page.add_tshirt_to_cart()
        main_page.add_onesie_to_cart()

        main_page.go_to_cart()
        cart_page.click_checkout()

        checkout_page.fill_personal_info(
            "Алла", "Морозова", "032203"
        )
        checkout_page.click_continue()

        total_price = checkout_page.get_total_price()

        assert total_price == "$58.29", f"Expected $58.29, but got {total_price}"

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

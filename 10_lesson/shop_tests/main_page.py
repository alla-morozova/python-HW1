from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_backpack = (
            By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']"
        )
        self.add_to_cart_tshirt = (
            By.XPATH,
            "//button[@data-test='add-to-cart-sauce-labs-bolt-t-shirt']"
        )
        self.add_to_cart_onesie = (
            By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-onesie']"
        )
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack_to_cart(self) -> None:
        """Добавляет рюкзак в корзину.

        Returns:
            None
        """
        backpack_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_to_cart_backpack)
        )
        backpack_btn.click()

    def add_tshirt_to_cart(self) -> None:
        """Добавляет футболку в корзину.

        Returns:
            None
        """
        tshirt_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_to_cart_tshirt)
        )
        tshirt_btn.click()

    def add_onesie_to_cart(self) -> None:
        """Добавляет комбинезон в корзину.

        Returns:
            None
        """
        onesie_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_to_cart_onesie)
        )
        onesie_btn.click()

    def go_to_cart(self) -> None:
        """Переходит в корзину.

        Returns:
            None
        """
        cart_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cart_link)
        )
        cart_link.click()

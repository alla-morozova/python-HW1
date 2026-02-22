import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def test_03_shop():
    firefox_options = FirefoxOptions()
    firefox_options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=firefox_options)
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)

    try:
        driver.get("https://www.saucedemo.com/")

        username = wait.until(EC.element_to_be_clickable((By.ID, "user-name")))
        username.send_keys("standard_user")

        password = wait.until(EC.element_to_be_clickable((By.ID, "password")))
        password.send_keys("secret_sauce")

        button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
        button.click()

        backpack = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
        backpack.click()

        shirt = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")))
        shirt.click()

        onesie = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-onesie")))
        onesie.click()

        container = wait.until(EC.element_to_be_clickable((By.ID, "shopping_cart_container")))
        container.click()

        checkout = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout.click()

        first_name = wait.until(EC.element_to_be_clickable((By.ID, "first-name")))
        first_name.send_keys("Алла")

        last_name = wait.until(EC.element_to_be_clickable((By.ID, "last-name")))
        last_name.send_keys("Морозова")

        postal_code = wait.until(EC.element_to_be_clickable((By.ID, "postal-code")))
        postal_code.send_keys("123456")

        continue_button = wait.until(EC.element_to_be_clickable((By.ID, "continue")))
        continue_button.click()

        total_element = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        total_text = total_element.text

        assert total_text == "Total: $58.29", f"Expected 'Total: $58.29', got '{total_text}'"
        print("Тест успешно пройден: сумма корректна.")

    finally:
        driver.quit()

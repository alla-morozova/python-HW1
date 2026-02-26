from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def enter_username(self, username):
        """Вводит логин в поле"""
        username_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.username_input)
        )
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        """Вводит пароль в поле"""
        password_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.password_input)
        )
        password_field.send_keys(password)

    def click_login(self):
        """Нажимает кнопку входа"""
        login_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        )
        login_btn.click()

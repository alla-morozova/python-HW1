from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_price = (By.CSS_SELECTOR, ".summary_total_label")

    def fill_personal_info(self, first_name, last_name, postal_code):
        first_name_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.first_name_input)
        )
        first_name_field.clear()
        first_name_field.send_keys(first_name)

        last_name_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.last_name_input)
        )
        last_name_field.clear()
        last_name_field.send_keys(last_name)

        postal_code_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.postal_code_input)
        )
        postal_code_field.clear()
        postal_code_field.send_keys(postal_code)

    def click_continue(self):
        continue_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.continue_button)
        )
        continue_btn.click()

    def get_total_price(self):
        total_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.total_price)
        )
        text = total_element.text
        price_str = text.split('$')[1].strip()
        return f"${price_str}"

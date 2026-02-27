from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

        self.delay_input = (By.ID, "delay")
        self.button_7 = (
            By.XPATH, "//span[@class='btn btn-outline-primary' and text()='7']"
        )
        self.button_plus = (By.XPATH, "//span[text()='+']")
        self.button_8 = (
            By.XPATH, "//span[@class='btn btn-outline-primary' and text()='8']"
        )
        self.button_equals = (By.XPATH, "//span[text()='=']")
        self.result_screen = (By.CSS_SELECTOR, ".screen")

    def open(self, url):
        self.driver.get(url)

    def set_delay(self, delay_value):
        element = self.wait.until(EC.element_to_be_clickable(self.delay_input))
        element.clear()
        element.send_keys(delay_value)

    def click_seven(self):
        button = self.wait.until(EC.element_to_be_clickable(self.button_7))
        button.click()

    def click_plus(self):
        button = self.wait.until(EC.element_to_be_clickable(self.button_plus))
        button.click()

    def click_eight(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.button_8)
        )
        button.click()

    def click_equals(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.button_equals)
        )
        button.click()

    def get_result(self):
        result_element = self.wait.until(
            EC.text_to_be_present_in_element(self.result_screen, "15")
        )
        result_element = self.driver.find_element(*self.result_screen)
        return result_element.get_attribute("textContent").strip()

import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def wind():

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.test_slow
def test_02_calc(wind):

    wait = WebDriverWait(wind, 60)

    wind.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    element = wind.find_element(By.ID, "delay")
    element.clear()
    element.send_keys("45")

    button_7 = wait.until(EC.element_to_be_clickable(
        (By.XPATH,
         "//span[@class='btn btn-outline-primary' and text()='7']")))
    button_7.click()

    button_plus = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='+']")))
    button_plus.click()

    button_8 = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[@class='btn btn-outline-primary' and text()='8']")))
    button_8.click()

    button_equals = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='=']")))
    button_equals.click()

    try:

        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

        result_element = wind.find_element(By.CSS_SELECTOR, ".screen")
        total = result_element.get_attribute("textContent").strip()

        assert total == "15", (
            f"\nТест не пройден! Ошибка калькулятора:\n"
            f"Ожидаемый результат: '15'\n"
            f"Получено: '{total}'\n"
        )
        print("Тест пройден, результат отобразился за 45 секунд")

    except TimeoutException:
        print("Ошибка: время ожидания истекло, результат не появился")
        raise
    finally:
        wind.quit()

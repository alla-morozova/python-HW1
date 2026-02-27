import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


@pytest.fixture
def wind():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.test_slow
def test_calculator_functionality(wind):
    calculator = CalculatorPage(wind)

    calculator.open(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    calculator.set_delay("45")

    calculator.click_seven()
    calculator.click_plus()
    calculator.click_eight()
    calculator.click_equals()

    result = calculator.get_result()
    assert result == "15", (
        f"\nТест не пройден! Ошибка калькулятора:\n"
        f"Ожидаемый результат: '15'\n"
        f"Получено: '{result}'\n"
    )

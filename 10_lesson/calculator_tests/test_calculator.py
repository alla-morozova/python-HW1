import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage
import allure


@pytest.fixture
def wind():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка работы калькулятора с задержкой")
@allure.description("Тест проверяет сложение чисел 7 и "
                    "8 в калькуляторе с установленной задержкой 45 с.")
@pytest.mark.test_slow
def test_calculator_functionality(wind):
    calculator = CalculatorPage(wind)

    with allure.step("Открываем страницу калькулятора"):
        calculator.open(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    with allure.step("Устанавливаем задержку 45 секунд"):
        calculator.set_delay("45")

    with allure.step("Нажимаем кнопки: 7, +, 8, ="):
        calculator.click_seven()
        calculator.click_plus()
        calculator.click_eight()
        calculator.click_equals()

    with allure.step("Получаем результат с экрана калькулятора"):
        result = calculator.get_result()

    with allure.step("Проверяем, что результат равен 15"):
        assert result == "15", (
            f"\nТест не пройден! Ошибка калькулятора:\n"
            f"Ожидаемый результат: '15'\n"
            f"Получено: '{result}'\n"
        )

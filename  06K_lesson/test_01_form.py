import pytest
from selenium import webdriver
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


def test_01_form(wind):

    wait = WebDriverWait(wind, 60)

    wind.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name=first-name]")))

    first_name = wind.find_element(By.CSS_SELECTOR, "[name=first-name]")
    first_name.send_keys("Иван")

    last_name = wind.find_element(By.CSS_SELECTOR, "[name=last-name]")
    last_name.send_keys("Петров")

    address = wind.find_element(By.CSS_SELECTOR, "[name=address]")
    address.send_keys("Ленина, 55-3")

    zip_code = wind.find_element(By.CSS_SELECTOR, "[name=zip-code]")
    zip_code.send_keys("")

    city = wind.find_element(By.CSS_SELECTOR, "[name=city]")
    city.send_keys("Москва")

    country = wind.find_element(By.CSS_SELECTOR, "[name=country]")
    country.send_keys("Россия")

    email = wind.find_element(By.CSS_SELECTOR, "[name=e-mail]")
    email.send_keys("test@skypro.com")

    phone_number = wind.find_element(By.CSS_SELECTOR, "[name=phone]")
    phone_number.send_keys("+7985899998787")

    job_position = wind.find_element(By.CSS_SELECTOR, "[name=job-position]")
    job_position.send_keys("QA")

    company = wind.find_element(By.CSS_SELECTOR, "[name=company]")
    company.send_keys("SkyPro")

    submit = wind.find_element(By.CSS_SELECTOR, "[type=submit]")
    submit.click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger")))

    zip_code_div = wait.until(EC.presence_of_element_located((By.ID, "zip-code")))
    assert "alert-danger" in zip_code_div.get_attribute("class"), "Поле Zip code не подсвечено красным"

    fields_to_check = [
        "first-name", "last-name", "address", "e-mail", "phone",
        "city", "country", "job-position", "company"
    ]

    for field_id in fields_to_check:
        field_div = wind.find_element(By.ID, field_id)
        assert "alert-success" in field_div.get_attribute("class"), f"Поле {field_id} не подсвечено зеленым"
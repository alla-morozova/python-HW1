# ЗАДАНИЕ: "Переименовать кнопку"
#Перейдите на сайт http://uitestingplayground.com/textinput.
#Укажите в поле ввода текст SkyPro.
#Нажмите на синюю кнопку.
#Получите текст кнопки и выведите в консоль ("SkyPro")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")

element = driver.find_element(By.ID, "newButtonName")
element.send_keys("SkyPro")

element2 = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
element2.click()

wait = WebDriverWait(driver, 20)
element3 = wait.until(EC.visibility_of_element_located((By.ID, "updatingButton")))

button_text = element2.text
print(button_text)

driver.quit()

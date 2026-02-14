# ЗАДАНИЕ: "Переименовать кнопку"
#Перейдите на сайт http://uitestingplayground.com/textinput.
#Укажите в поле ввода текст SkyPro.
#Нажмите на синюю кнопку.
#Получите текст кнопки и выведите в консоль ("SkyPro")


from time import sleep #импортировали метод из пакета
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By #не забудьте импортировать класс By

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

driver.get(" http://uitestingplayground.com/textinput")

element = driver.find_element(By.ID, "newButtonName")
element.send_keys("SkyPro")

element2 = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
element2.click()

button_text = element2.text
print(button_text)

driver.quit()

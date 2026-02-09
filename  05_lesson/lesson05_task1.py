from time import sleep #импортировали метод из пакета
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

#зайти на сайт
driver.get("http://uitestingplayground.com/classattr")
sleep(4)
#нам нужно найти нужную кнопку
element = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
#Кликнуть на синюю кнопку
element.click()
sleep(4)
#закрыть браузер
driver.quit()

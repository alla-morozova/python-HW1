from time import sleep #импортировали метод из пакета
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()


driver.get("http://uitestingplayground.com/dynamicid")
sleep(4)

# нам нудно найти нужную кнопку
element = driver.find_element(By.CSS_SELECTOR, ".btn-primary")

element.click()
sleep(4)

driver.quit()

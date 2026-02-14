from time import sleep #импортировали метод из пакета
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.maximize_window()

driver.get(" http://the-internet.herokuapp.com/login")
sleep(6)

element = driver.find_element(By.ID, "username")
element.send_keys("tomsmith")

element = driver.find_element(By.ID, "password")
element.send_keys("SuperSecretPassword!")
sleep(3)

element = driver.find_element(By.CSS_SELECTOR, "button.radius")
element.click()
sleep(6)

element = driver.find_element(By.ID, "flash")
text = element.get_attribute("textContent").strip()

print(text[:-1])

driver.quit()

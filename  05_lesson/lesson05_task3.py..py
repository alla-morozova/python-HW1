from time import sleep #импортировали метод из пакета
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/inputs")
sleep(6)

element = driver.find_element(By.CSS_SELECTOR, "input")
element.send_keys("Sky")
sleep(3)

element.clear()
sleep(3)

element.send_keys("Pro")
sleep(3)

driver.quit()

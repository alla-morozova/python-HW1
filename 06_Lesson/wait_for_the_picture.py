#Задание:Дождаться картинки
# Перейдите на сайт https://bonigarcia.dev/selenium-webdriver-java/loading-images.html.
# Дождитесь загрузки всех картинок.
# Получите значение атрибута src у 3-й картинки.
# Выведите значение в консоль.

from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

driver.get(" https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

waiter = WebDriverWait(driver,40)
images1 = waiter.until(EC.visibility_of_element_located((By.ID, "compass")))
images2 = waiter.until(EC.visibility_of_element_located((By.ID, "calendar")))
images3 = waiter.until(EC.visibility_of_element_located((By.ID, "award")))
images4 = waiter.until(EC.visibility_of_element_located((By.ID, "landscape")))

src_images3 = driver.find_element(By.ID,"award").get_attribute("src")
print(src_images3)

driver.quit()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query="laptop"
driver.get("https://www.limeroad.com/search/jeans")
elem = driver.find_element(By.CLASS_NAME, "conW  ")
print(elem.text)
time.sleep(42)
driver.close()
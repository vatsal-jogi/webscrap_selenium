from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://news.abplive.com/sports")
elem = driver.find_elements(By.CLASS_NAME, "story-wrapper ")
print(f"Total elements found: {len(elem)}")
for i in elem:
   d=i.get_attribute("outerHTML")
   with open(f"data/data.html","a",encoding="utf-8") as f:
       f.write(d)
time.sleep(4)
driver.close()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import json

driver = webdriver.Chrome()
driver.get("https://news.abplive.com/sports")
elem = driver.find_elements(By.CLASS_NAME, "story-wrapper")
print(f"Total elements found: {len(elem)}")

def get_product_data():
    data = {}
    for index, i in enumerate(elem):
        label = i.find_element(By.CLASS_NAME, "story-labels-category-name").text
        title = i.find_element(By.CLASS_NAME, "story-title").text
        
        data[f"News{index}"] = {
            "label": label,
            "title": title
        }
        
    return json.dumps(data, indent=4)

def save_product_data_to_json(filename):
    json_output = get_product_data()
    
    with open(filename, 'w') as json_file:
        json_file.write(json_output)

# Call the function to save the data to a JSON file
save_product_data_to_json('News_data.json')

time.sleep(4)
driver.close()
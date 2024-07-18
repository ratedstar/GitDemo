import time

from selenium.webdriver.common.by import By
from selenium import webdriver

URL ="https://www.hotwire.com/"
baseURL = "https://www.letskodeit.com/practice"
driver = webdriver.Firefox()
driver.get(URL)
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//div[contains(@class,'location-typeahead')]//div/input[@type='text']").send_keys("del")
#ulElement = driver.find_element(By.XPATH,'//ul[contains(@class,"dropdown")]')
#innerhtml = ulElement.get_attribute("innerHTML")
lielements = driver.find_elements(By.XPATH,'//ul[contains(@class,"dropdown")]/li/a')
destination = "Delh"
for element in lielements:
    if destination in element.text:
        element.click()
        break

driver.quit()
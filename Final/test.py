from selenium import webdriver
from selenium.webdriver.common.by import By

class test():
    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

t1 = test()
t1.test()

# FileUpload Using PYNPUT and without PYNPUT
from pynput.keyboard import Controller, Key
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test:
        def testUpload(self):
                driver = webdriver.Firefox()
                # baseURL = "https://www.plupload.com/examples/"
                # # baseURL = "https://imgbb.com/upload"
                # driver.get(baseURL)
                # driver.find_element(By.ID, "uploader_browse").click()
                #
                # element = driver.find_element(By.ID, "//div[@id='uploader_buttons']/div/input")
                # element.send_keys("C:\\Users\\HP\\Downloads\\Python_Sample_Images\\sample1.png")
                # keyboard = Controller()
                # keyboard.type("C:\\Users\\HP\\Downloads\\Python_Sample_Images\\sample1.png")
                # keyboard.press(Key.enter)
                # keyboard.release(Key.enter)

                driver.implicitly_wait(3)
                driver.maximize_window()
                driver.get("https://www.plupload.com/examples/")
                element = driver.find_element(By.ID,"anywhere-upload-input")
                element.send_keys("C:\\Users\\HP\\Downloads\\Python_Sample_Images\\sample.png")
                l=driver.find_element_by_id("btn");
                l.click();
                #with JavaScript Executor
                driver.execute_script("arguments[0].click();", l);
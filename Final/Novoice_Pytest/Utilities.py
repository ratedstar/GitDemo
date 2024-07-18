from selenium.webdriver.common.by import By


class HandyWrapers():
    def __init__(self,driver):
        self.driver = driver

    def getByType(self,locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "tagname":
            return By.TAG_NAME
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "cssselector":
            return By.CSS_SELECTOR
        elif locatorType == "linktest":
            return By.LINK_TEXT
        elif locatorType == "Partiallinktest":
            return By.PARTIAL_LINK_TEXT
        else:
            print("Invalid locatorType please enter a valid one")
        return False
    def getElement(self,locator, locatorType='id'):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType,locator)
            print("Element found")
        except:
            print("Element not found ")
        return element
    def elementPresent(self,locator,byType):
        try:
            element = self.driver.find_element(byType,locator)
            if element is not None:
                print("Element Found")
                return True
            else:
                return False
        except:
            print("Element not found")
            return False
    def elementsPresence(self,locator,byType):
        try:
            elementlst = self.driver.find_elements(byType,locator)
            if len(elementlst) > 0:
                print("Elements found")
                return True
            else:
                print("Element not found")
                return False
        except:
            print("Element not found")
            return False







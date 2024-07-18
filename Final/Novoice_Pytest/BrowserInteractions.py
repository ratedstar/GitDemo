import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Novoice_Pytest.Utilities import HandyWrapers
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import  *
from ScreenShotGeneric import Screenshot
from pynput.keyboard import Key, Controller
from selenium.webdriver import ActionChains
class ClickAndSendKeys():
    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "//a[@href='/login']").click()
        driver.find_element(By.ID, "email").send_keys("test")
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("test")
        driver.find_element(By.ID, "login").click()
        time.sleep(5)
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.find_element(By.ID,'login').click()
        driver.find_element(By.XPATH,"//input[@name='password']").send_keys("Test")
        driver.find_element(By.ID,'email').send_keys("test")
        driver.find_element(By.ID,"login").click()

    def test_radio(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(10)
        radiolst=driver.find_elements(By.XPATH,'//input[@type="radio"]')
        radiolsts = driver.find_elements(By.XPATH,"//input[@type='radio']")
        for radio in radiolst:
            if radio.is_selected()!= True:
                radio.click()
    def test_select(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(10)
        print("Select benz by value")
        element = driver.find_element(By.ID,"carselect")
        element = driver.find_element(By.ID,"car")
        sel = Select(element)
        sel.select_by_value("bmw")
        time.sleep(2)
        print("Select honda by index")
        sel.select_by_index(1)
        time.sleep(2)
        print("select Bmv by visible text")
        sel.select_by_visible_text("BMW")
        time.sleep(2)
    def test_elementPresence(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(10)
        elementText=driver.find_element(By.XPATH,"//a[contains(text(),'Open Tab')]").text
        print(elementText)
        elementAttribute = driver.find_element(By.ID,"name").get_attribute("placeholder")
        print(elementAttribute)
        driver.find_element(By.ID,"hide-textbox").click()
        stateofele = driver.find_element(By.ID,"displayed-text").is_displayed()
        print(stateofele,"hide")
        elementState=driver.find_element(By.ID,"show-textbox")
        print(elementState)
        #driver.find_element(By.ID,"show-textbox").click()
        stateofele = driver.find_element(By.ID, "displayed-text").is_displayed()
        print(stateofele,"show")
        if stateofele == True:
            driver.find_element(By.ID,"displayed-text").send_keys("Test")
        driver.quit()
    #Dynamic xpath
    def testdyanamicxpath(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(10)
        button = "//a[contains(text(),'{0}')]"
        allcourses = button.format("ALL COURSES")
        driver.find_element(By.XPATH,allcourses).click()
        course = "//h4[contains(@class,'dynamic-heading')and contains(text(),'{0}')]"
        courselocator = course.format("JavaScript for beginners")
        driver.find_element(By.XPATH,courselocator).click()
        driver.find_element(By.ID,"search").send_keys("Java script")
        driver.quit()
    # Explicit Wait
    def test_Explicitwait(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        #driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.execute_script("window.location='https://www.letskodeit.com/';")
        wait = WebDriverWait(driver, timeout=10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH,"//a[contains(text(),'Sign In')]")))
        element.click()
    # Explicit Wait or fluent wait
    def test_Fluentwait(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        #driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.execute_script("window.location='https://www.letskodeit.com/';")
        wait = WebDriverWait(driver,timeout=10,poll_frequency=1,ignored_exceptions=[NoSuchElementException,
                                                                                    ElementNotVisibleException,
                                                                                    ElementNotSelectableException])
        element = wait.until(EC.visibility_of_element_located((By.XPATH,"//a[contains(text(),'Sign In')]")))
        element.click()
    # FileUpload Using PYNPUT and without PYNPUT
    #from pynput.keyboard import Key, Controller
    def testUpload(self):
        driver = webdriver.Firefox()
        baseURL = "https://www.plupload.com/examples/"
        #baseURL = "https://imgbb.com/upload"
        driver.get(baseURL)
        #driver.find_element(By.ID,"uploader_browse").click()

        # element= driver.find_element(By.ID, "//div[@id='uploader_buttons']/div/input")
        # element.send_keys("C:\\Users\\HP\\Downloads\\Python_Sample_Images\\sample.png")
        # keyboard = Controller()
        # keyboard.type("C:\\Users\\HP\\Downloads\\Python_Sample_Images\\sample.png")
        # keyboard.press(Key.enter)
        # keyboard.release(Key.enter)

        element = driver.find_element(By.ID,"")
        keyboard = Controller()
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get("https://imgbb.com/upload")
        element = driver.find_element(By.ID, "anywhere-upload-input")
        element.send_keys("C:\\Users\\HP\\Downloads\\Python_Sample_Images\\sample.png")
    def testCalender(self):
        driver = webdriver.Firefox()
        baseURL = "https://www.expedia.co.in/"
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH,"//span[contains(text(),'Flights')]").click()
        driver.find_element(By.XPATH,"//div[contains(@class,'uitk-field has-floatedLabel-label has-icon has-placeholder')][1]").click()
        datelist = driver.find_elements(By.XPATH,'//div[@class="uitk-month uitk-month-double uitk-month-double-left"]//tr/td')
        for date in datelist:
            if date.text =="2":
                date.click()

        #driver.find_element(By.XPATH,"//div[@class='uitk-month uitk-month-double uitk-month-double-left']//tr/td//div[contains(text(),'2')]").click()
    #Auto complete dynamic dropdowns
    def testDynamicDropDown(self):
        driver = webdriver.Firefox()
        baseURL = "https://www.goibibo.com/flights/"
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(3)
        parText = "del"
        textToSelect = "New Delhi"
        driver.find_element(By.XPATH, "//span[@class='sc-gsFSXq bGTcbn']").click()
        driver.find_element(By.XPATH, "//p[contains(text(),'Enter city or airport')][1]").click()
        time.sleep(4)
        #while using position use () main xpath with parenthesis
        driver.find_element(By.XPATH,"(//input[@type='text'])[position() = 1]").send_keys(parText)
        ulelement = driver.find_element(By.ID,"autoSuggest-list")
        innerHTML = ulelement.get_attribute("innerHTML")
        print(innerHTML)

        liElements = ulelement.find_elements(By.TAG_NAME, "li")
        time.sleep(2)
        for element in liElements:
            if textToSelect in element.text:
                element.click()
                break
        time.sleep(4)
        driver.quit()

        #Taking Screenshot
    def testTakescreenshot(self):
        driver=webdriver.Firefox()
        baseURL = "https://www.letskodeit.com/practice"
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH,'(//a[contains(text(),"Sign In")])[position() = 1]').click()
        driver.find_element(By.ID,"email").send_keys("test")
        driver.find_element(By.ID,'login-password').send_keys()
        driver.find_element(By.ID,'login').click()
        ScreenShot = Screenshot()
        ScreenShot.takeScreenshot(driver)

    def windowSize(self):
        driver= webdriver.Firefox()
        baseURL = "https://www.letskodeit.com/practice"
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(5)
        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth;")
        print("Height::"+str(height))
        print("Width::"+str(width))

    def scrollPage(self):
        driver = webdriver.Firefox()
        baseURL = "https://www.letskodeit.com/practice"
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(5)
        # scroll page down
        driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(2)
        #scroll page up
        driver.execute_script("window.scrollBy(0,-1000);")
        time.sleep(3)
        #scroll a particular element
        element = driver.find_element(By.ID,'mousehover')
        driver.execute_script("arguments[0].scrollIntoView(true);",element)
        time.sleep(5)
        driver.execute_script("window.scrollBy(0,-150)")
        #native method to scroll
        driver.execute_script("window.scrollBy(0,-1000)")
        time.sleep(5)
        location = element.location_once_scrolled_into_view
        print("locaton::"+str(location))

    def switchWindow(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)

        # Find parent handle -> Main Window
        parentHandle = driver.current_window_handle
        print("Parent Handle: " + parentHandle)
        parentHandle = driver.current_window_handle


        # Find open window button and click it
        driver.find_element(By.ID, "openwindow").click()
        time.sleep(2)

        # Find all handles, there should two handles after clicking open window button
        handles = driver.window_handles

        # Switch to window and search course
        for handle in handles:
            print("Handle: " + handle)
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                print("Switched to window:: " + handle)
                time.sleep(2)
                driver.find_element(By.XPATH,"//a[contains(text(),'Sign In')]").click()
                # searchBox = driver.find_element(By.ID, "search")
                # searchBox.click()
                # time.sleep(2)
                #searchBox.send_keys("python")
                time.sleep(2)
                driver.close()
                break

        # Switch back to the parent handle
        driver.switch_to.window(parentHandle)
        driver.find_element(By.ID, "name").send_keys("Test Successful")

    def switchToIframe(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.execute_script("window.scrollBy(0,1000);")
        #Switch to iframe using id
        #driver.switch_to.frame("courses-iframe")
        # Switch to iframe using name
        #driver.switch_to.frame("iframe-name")
        #switch to iframe using number
        driver.switch_to.frame(0)
        # Search course
        driver.find_element(By.XPATH,"//a[contains(text(),'Sign In')]").click()
        time.sleep(2)
        #Switch to default content
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0,-1000);")
        driver.find_element(By.ID,'autosuggest').send_keys("test")

    def handlingJavaScriptPopups(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.find_element(By.ID,'name').send_keys("lamp")
        driver.find_element(By.ID,"alertbtn").click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(1)
        driver.find_element(By.ID,'name').send_keys("lion")
        driver.find_element(By.ID,"confirmbtn").click()
        time.sleep(2)
        driver.switch_to.alert.dismiss()
        time.sleep(2)
    def mouseover(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        element = driver.find_element(By.ID,'mousehover')
        topElement = driver.find_element(By.XPATH,"//a[contains(text(),'Top')]")
        driver.execute_script("window.scrollBy(0,300);")
        time.sleep(2)
        try:
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            print("MouseOvered on Element")
            time.sleep(2)
            actions.move_to_element(topElement).click().perform()
            print("Item Clicked")
        except:
            print("Mouse overed on element")

    def dragDrop(self):
        baseUrl = "https://jqueryui.com/droppable/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        driver.switch_to.frame(0)
        fromElement =driver.find_element(By.XPATH,"//div/p[contains(text(),'Drag me to my target')]")
        toElement = driver.find_element(By.ID,'droppable')
        try:
            actions = ActionChains(driver)
            #actions.drag_and_drop(fromElement,toElement).perform()
            actions.click_and_hold(fromElement).move_to_element(toElement).release().perform()
            time.sleep(2)
        except:
            print("Element was to dropped")
    def slider(self):
        baseUrl = "https://jqueryui.com/slider/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        driver.switch_to.frame(0)
        slider = driver.find_element(By.XPATH,'//div[@id="slider"]/span')
        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(slider,100,0).perform()
            print("Slider element successful")
            time.sleep(2)
        except:
            print("Sliding failed")


ff = ClickAndSendKeys()
ff.slider()


"""
Other ways to click a button
l=driver.find_element_by_id("btn");
l.click();
//with JavaScript Executor
driver.execute_script("arguments[0].click();", l);
"""
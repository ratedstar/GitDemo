#radioButton
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait, expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager



class SeleniumBasics:
    def test_radioBtn(self):
        baseUrl = "https://rahulshettyacademy.com/AutomationPractice/"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(10)
        radioBtns= driver.find_elements(By.XPATH,"//input[@name='radioButton']")
        for radio in radioBtns:
            if radio.is_selected() != True:
                print(radio.get_attribute('value'))
                print(radio.get_property('name'))
                if radio.get_attribute('value') == 'radio1':
                    radio.click()
                    driver.close()
                    break

    def test_dropDown(self):
        baseUrl = "https://rahulshettyacademy.com/AutomationPractice/"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(10)
        dropdown = driver.find_element(By.XPATH,"//select[@id='dropdown-class-example']")
        sel = Select(dropdown)
        #By index
        sel.select_by_index(1)
        time.sleep(2)
        #By value
        sel.select_by_value('option2')
        time.sleep(2)
        #By visible text
        sel.select_by_visible_text('Option3')
        time.sleep(2)
        sel.select_by_index(1)
        driver.close()
    def test_checkBox(self):
        baseUrl = "https://rahulshettyacademy.com/AutomationPractice/"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(10)
        checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
        print(len(checkboxes))
        for checkbox in checkboxes:
            print(checkbox.get_attribute('value'))
            if checkbox.get_attribute('value') == 'option2':
                print(checkbox.text)
                checkbox.click()
                driver.close()
                #assert checkbox.is_selected()

    def test_AutosuggestDynamicDropdowns(self):
        baseUrl = "https://rahulshettyacademy.com/dropdownsPractise/"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.find_element(By.ID,'autosuggest').send_keys('ind')
        countrieslist = driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']/a")
        for country in countrieslist:
            if country.text == 'India':
                country.click()
                driver.close()
                break

    def test_alertBox(self):
        baseUrl = "https://rahulshettyacademy.com/AutomationPractice/"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.find_element(By.ID,'name').send_keys('Test')
        driver.find_element(By.ID,'alertbtn').click()
        time.sleep(3)
        driver.switch_to.alert.accept()
        time.sleep(2)
        driver.find_element(By.ID,'confirmbtn').click()
        time.sleep(2)
        driver.switch_to.alert.dismiss()
        driver.close()
    def test_iframe(self):
        baseUrl = "https://rahulshettyacademy.com/AutomationPractice/"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.execute_script('window.scrollBy(0,1000)')
        time.sleep(2)
        driver.switch_to.frame('courses-iframe')
        driver.find_element(By.XPATH,"//a[contains(text(), 'Practice')]").click()
        time.sleep(2)
        driver.switch_to.default_content()
        driver.find_element(By.ID,'name').send_keys('test')
        time.sleep(3)
        driver.close()
    def test_mouseover(self):
        baseUrl = 'https://rahulshettyacademy.com/AutomationPractice/'
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.execute_script('window.scrollBy(0,850)')
        element = driver.find_element(By.ID,'mousehover')
        topElement = driver.find_element(By.XPATH,"//a[contains(text(),'Top')]")
        try:
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            print("Mouse Overed on element")
            actions.move_to_element(topElement).click().perform()
            print('Item got clicked')
        except:
            print("Mouse over not working")
        driver.close()
    def test_waits(self):
        baseUrl = "https://rahulshettyacademy.com/seleniumPractise/#/"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH,"//input[@type='search']").send_keys('ber')
        time.sleep(5)
        selectedproducts = driver.find_elements(By.XPATH,"//div[@class='products']/div")
        for product in selectedproducts:
            product.find_element(By.XPATH,"div/button").click()
        driver.find_element(By.XPATH,"//a[@class='cart-icon']").click()
        driver.find_element(By.XPATH,"//button[contains(text(),'PROCEED TO CHECKOUT')]").click()
        driver.find_element(By.XPATH,"//input[@class='promoCode']").send_keys('rahulshettyacademy')
        driver.find_element(By.XPATH,"//button[@class='promoBtn']").click()
        # verify success message
        wait = WebDriverWait(driver,10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//span[contains(text(),'Code applied ..!')]")))
        driver.find_element(By.XPATH,"//button[contains(text(),'Place Order')]").click()
        driver.close()
    #verify sum of cart products
    def test_cartValidation(self):
        baseUrl = "https://rahulshettyacademy.com/seleniumPractise/#/"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.find_element(By.CLASS_NAME,'search-keyword').send_keys('ber')
        time.sleep(3)
        searchproducts = driver.find_elements(By.XPATH,"//div[@class='products']/div")
        for product in searchproducts:
            product.find_element(By.XPATH,'div/button').click()
        driver.find_element(By.CLASS_NAME,"cart-icon").click()
        driver.find_element(By.XPATH,"//button[contains(text(),'PROCEED TO CHECKOUT')]").click()
        cartitems = driver.find_elements(By.CSS_SELECTOR,'tr td:nth-child(5) p')
        sum = 0
        for item in cartitems:
            sum += int(item.text)
        totalamt = driver.find_element(By.CLASS_NAME,'totAmt').text
        assert sum == int(totalamt)
        driver.close()

    def test_addcartValidation(self):
        baseUrl = "https://rahulshettyacademy.com/seleniumPractise/#/"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.find_element(By.CLASS_NAME, 'search-keyword').send_keys('ber')
        time.sleep(3)
        cartproducts= driver.find_elements(By.XPATH,"//div[@class='products']/div")
        for product in cartproducts:
            product.find_element(By.XPATH,"div/button").click()
        driver.find_element(By.XPATH,"//a[@class='cart-icon']").click()
        driver.find_element(By.XPATH,"//button[contains(text(),'PROCEED TO CHECKOUT')]").click()
        driver.find_element(By.CLASS_NAME,"promoCode").send_keys("rahulshettyacademy")
        driver.find_element(By.CLASS_NAME,"promoBtn").click()
        wait = WebDriverWait(driver,10)
        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoInfo")))
        totalamount = driver.find_element(By.CLASS_NAME,"totAmt").text
        discounttotal = driver.find_element(By.CLASS_NAME,"discountAmt").text
        assert float(discounttotal)< float(totalamount)
        driver.close()

    def test_verifyCartItems(self):
        baseUrl = "https://rahulshettyacademy.com/seleniumPractise/#/"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)
        expectedlist = []
        driver.find_element(By.CLASS_NAME, 'search-keyword').send_keys('ber')
        time.sleep(3)
        cartproducts = driver.find_elements(By.XPATH, "//div[@class='products']/div")
        for product in cartproducts:
            expectedlist.append(product.find_element(By.XPATH,"h4").text)
            print(expectedlist)
            product.find_element(By.XPATH, "div/button").click()
        driver.find_element(By.XPATH, "//a[@class='cart-icon']").click()
        driver.find_element(By.XPATH, "//button[contains(text(),'PROCEED TO CHECKOUT')]").click()
        cartlist = driver.find_elements(By.XPATH,"//tr/td[2]/p")
        actuallist = []
        for item in cartlist:
            actuallist.append(item.text)
        print(actuallist)
        assert expectedlist == actuallist
        driver.close()
    def test_childwindow(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)
        Parenthandle = driver.current_window_handle
        driver.find_element(By.ID,"openwindow").click()
        time.sleep(5)
        windows= driver.window_handles
        for window in windows:
            if window not in Parenthandle:
                driver.switch_to.window(window)
                #time.sleep(3)
                driver.find_element(By.XPATH,"//a[contains(text(),'Sign In')]").click()
                driver.close()
        driver.switch_to.window(Parenthandle)
        driver.find_element(By.ID,"autosuggest").send_keys("Test")

    def test_assignmentNewtab(self):
        samplestring = "i am kamesh my email id kaameshindraganti@gmail.com lets drop a mail"
        grablist = samplestring.split(" ")
        baseUrl = "https://www.rahulshettyacademy.com/"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)
        email=" "
        for item in grablist:
            if item.__contains__("@gmail.com"):
                email = item
        time.sleep(3)
        driver.find_element(By.XPATH,"//a[contains(@class,'theme-btn register-btn')]").click()
        driver.find_element(By.ID,'email').send_keys(email)
        time.sleep(3)
        driver.close()
    def test_sortwebtables(self):
        baseUrl = "https://rahulshettyacademy.com/seleniumPractise/#/"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH,"//a[contains(text(),'Top Deals')]").click()
        # parent handle
        ParentHandle=driver.current_window_handle
        # all handles
        handles = driver.window_handles
        time.sleep(3)
        print(len(handles))
        # windowsOpened = driver.window_handles
        # driver.switch_to.window(windowsOpened[1])
        # time.sleep(3)
        # driver.find_element(By.XPATH, "//input[@id='search-field']").click()
        browsersorted = []
        for handle in handles:
            if handle not in ParentHandle:
                driver.switch_to.window(handle)
                time.sleep(3)
                driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
        listofveggies = driver.find_elements(By.XPATH,"//tbody/tr/td[1]")
        for item in listofveggies:
            browsersorted.append(item.text)
        originalveggielist = browsersorted.copy()
        #now lets sort
        browsersorted.sort()
        assert originalveggielist == browsersorted
        driver.close()
    def test_chromeOptions(self):
        baseUrl = "https://rahulshettyacademy.com/seleniumPractise/#/"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        #chrome_options.add_argument("headless")
        chrome_options.add_argument("--ignore-certificate-errors")
        driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
        driver.get(baseUrl)
        print(driver.title)
    def test_e2e1(self):
        baseUrl = "https://rahulshettyacademy.com/angularpractice/"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        #chrome_options.add_argument("headless")
        chrome_options.add_argument("--ignore-certificate-errors")
        driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
        driver.get(baseUrl)
        driver.find_element(By.XPATH,"//div/input[@name='name']").send_keys("Kaamesh")
        driver.find_element(By.XPATH,"//div/input[@name='email']").send_keys("kaamesh123@gmail.com")
        driver.find_element(By.ID,"exampleInputPassword1").send_keys("Test")
        driver.find_element(By.ID,"exampleCheck1").click()
        sel = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
        sel.select_by_visible_text("Female")
        driver.find_element(By.XPATH,"//label[text()='Student']").click()
        driver.find_element(By.XPATH,"//input[@name='bday']").send_keys("22/03/2003")
        driver.find_element(By.XPATH,"//input[@type='submit']").click()
        time.sleep(3)
    def test_shopExmpl(self):
        baseUrl = "https://rahulshettyacademy.com/angularpractice/"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--ignore-certificate-errors")
        driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
        driver.get(baseUrl)
        driver.find_element(By.XPATH,"//a[text()='Shop']").click()
        driver.implicitly_wait(3)
        products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
        for product in products:
            productName = product.find_element(By.XPATH,"div/h4/a")
            if productName.text == "Blackberry":
                driver.execute_script("window.scrollBy(0,850)")
                product.find_element(By.XPATH,"div/button").click()
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,-1000)")
        driver.find_element(By.XPATH,"//a[contains(text(),'Checkout ')]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[contains(text(),'Checkout ')]").click()
        driver.find_element(By.ID,"country").send_keys("ind")
        wait = WebDriverWait(driver,10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
        driver.find_element(By.LINK_TEXT,"India").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//label[contains(text(),'I agree with the ')]").click()
        driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
        time.sleep(3)
        successmsg = driver.find_element(By.CLASS_NAME,"alert-success").text
        print(successmsg)
        assert "Success! Thank you!" in successmsg
    def test_Assinment(self):
        pass




callselenium = SeleniumBasics()
#callselenium.test_dropDown()
callselenium.test_radioBtn()
#callselenium.test_AutosuggestDynamicDropdowns()
#callselenium.test_checkBox()
#callselenium.test_alertBox()
#callselenium.test_iframe()
#callselenium.test_mouseover()
#callselenium.test_waits()
#callselenium.test_cartValidation()
#callselenium.test_addcartValidation()
#callselenium.test_verifyCartItems()
#callselenium.test_childwindow()
#callselenium.test_assignmentNewtab()
#callselenium.test_sortwebtables()
#callselenium.test_chromeOptions()
#callselenium.test_e2e1()
callselenium.test_shopExmpl()





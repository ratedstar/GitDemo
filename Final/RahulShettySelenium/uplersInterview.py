import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


class swaglabs:
    def sort_products_z2a(self):
        baseUrl = "https://www.saucedemo.com/inventory.html"
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        Dropdown = driver.find_element(By.CSS_SELECTOR, ".product_sort_container")
        sel = Select(Dropdown)
        sel.select_by_value("za")
        products = driver.find_elements(By.CSS_SELECTOR, ".inventory_item_label a")
        list_of_products = []
        for product in products:
            list_of_products.append(product.text)
        print(list_of_products)
        original_browser_sorted_z2a__products = list_of_products.copy()
        list_of_products.sort(reverse=True)
        assert original_browser_sorted_z2a__products == list_of_products
        driver.close()
    def sort_price_lohi(self):
        baseUrl = "https://www.saucedemo.com/inventory.html"
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        Dropdown = driver.find_element(By.CSS_SELECTOR, ".product_sort_container")
        sel = Select(Dropdown)
        sel.select_by_value("lohi")
        # list1.sort()
        list_of_prices = []
        # lohi
        pricelist = driver.find_elements(By.CSS_SELECTOR, ".inventory_item_price")
        for price in pricelist:
            list_of_prices.append(float(price.text.lstrip('$')))
        list_of_prices = [float(i) for i in list_of_prices]
        original_browser_sorted_lo2hi__price = list_of_prices.copy()
        list_of_prices.sort()
        print(list_of_prices)
        assert original_browser_sorted_lo2hi__price == list_of_prices
        driver.close()
    def sort_price_hilo(self):
        baseUrl = "https://www.saucedemo.com/inventory.html"
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        Dropdown = driver.find_element(By.CSS_SELECTOR, ".product_sort_container")
        sel = Select(Dropdown)
        sel.select_by_value("hilo")
        # list1.sort()
        list_of_prices = []
        pricelist = driver.find_elements(By.CSS_SELECTOR, ".inventory_item_price")
        for price in pricelist:
            list_of_prices.append(float(price.text.lstrip('$')))
        list_of_prices = [float(i) for i in list_of_prices]
        original_browser_sorted_hi2lo__price = list_of_prices.copy()
        list_of_prices.sort(reverse=True)
        print(list_of_prices)
        assert original_browser_sorted_hi2lo__price == list_of_prices
        driver.close()
    def sort_products_a2z(self):
        baseUrl = "https://www.saucedemo.com/inventory.html"
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        Dropdown = driver.find_element(By.CSS_SELECTOR, ".product_sort_container")
        sel = Select(Dropdown)
        sel.select_by_value("za")
        time.sleep(3)
        sel.select_by_value("az")
        products = driver.find_elements(By.CSS_SELECTOR, ".inventory_item_label a")
        list_of_products = []
        for product in products:
            list_of_products.append(product.text)
        print(list_of_products)
        original_browser_sorted_a2z__products = list_of_products.copy()
        list_of_products.sort()
        assert original_browser_sorted_a2z__products == list_of_products
        driver.close()

    def logout(self):
        baseUrl = "https://www.saucedemo.com/inventory.html"
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        driver.find_element(By.ID,"react-burger-menu-btn").click()
        driver.find_element(By.ID,"logout_sidebar_link").click()
    def resetApp(self):
        baseUrl = "https://www.saucedemo.com/inventory.html"
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        #Sauce Labs Bike Light
        products = driver.find_elements(By.CSS_SELECTOR, ".inventory_item_label a")
        for product in products:
            if product.text == "Sauce Labs Bike Light":
                driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click()
                break
        time.sleep(3)
        #reset_sidebar_link
        items_in_cart= driver.find_element(By.CSS_SELECTOR,"#shopping_cart_container a span")
        items_in_cart.is_displayed()
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        driver.find_element(By.ID, "reset_sidebar_link").click()
        driver.find_element(By.ID,'react-burger-cross-btn').click()
        # try:
        #     driver.find_element(By.CSS_SELECTOR,"#shopping_cart_container a span").is_displayed()
        #     raise Exception
        # except Exception as e:
        #     print(e)
        #     print("Chart is empty")
        try:
            driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container a span").is_displayed()
        except:
            print("Chart is empty")
        time.sleep(3)
        driver.close()
    def end2end(self):
        baseUrl = "https://www.saucedemo.com/inventory.html"
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        products = driver.find_elements(By.CSS_SELECTOR, ".inventory_item_label a")
        for product in products:
            if product.text == "Sauce Labs Bike Light":
                product.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]").click()
                break
        driver.find_element(By.ID,"shopping_cart_container").click()
        time.sleep(2)
        driver.find_element(By.ID,"checkout").click()
        time.sleep(2)
        driver.find_element(By.ID,"first-name").send_keys("test")
        driver.find_element(By.ID,"last-name").send_keys("test")
        driver.find_element(By.ID,"postal-code").send_keys("50090")
        driver.find_element(By.ID,"continue").click()
        time.sleep(2)
        driver.find_element(By.ID,"finish").click()
        sucessmsg = driver.find_element(By.XPATH,"//div[@id='checkout_complete_container']/h2").text
        actualmsg = "Thank you for your order!"
        assert sucessmsg == actualmsg
        driver.find_element(By.ID,"back-to-products").click()
        driver.find_element(By.XPATH,"//div[contains(text(),'Swag Labs')]").is_displayed()
        time.sleep(2)


sg = swaglabs()
sg.resetApp()




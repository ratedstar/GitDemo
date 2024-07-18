"""
text()
//input[@class="Hero-Homepage"]//a[text()='Yoga']
contains()
//div[@id='navbar']//a[contains(text(),'Login')]
//div[@id='navbar']//a[contains(@class,'navbar-link') and contains(@href,'signIn')
starts-with
//div[starts-with(@class,'name')
parent::preceding-sibling::following-sibling
//a[contains(text(),"ALL COURSES")]//parent::li//preceding-sibling::li//following-sibling::li[3]

"""
from selenium import webdriver


def test_Method():
    baseURl = ""
    driver = webdriver.Firefox()

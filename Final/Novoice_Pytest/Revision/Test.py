from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Novoice_Pytest.Utilities import HandyWrapers
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import  *
from pynput.keyboard import Key, Controller
from selenium.webdriver import ActionChains

'''lengthy_str = "this is the lengthy string to test the search def"
search_word = "test"
def search_str(lengthy_str, search_word):
    <logic goes here>
output = {
    "t": (num of occ, [indices]),
    "e": (num of occ, [indices]),
    "s": (num of occ, [indices]),
    "te": (num of occ, [indices]),
    "tes": (num of occ, [indices]),
    "test": (num of occ, [indices]),
}
'''
lengthy_str = "this is the lengthy string to test the search def"
search_word = "test"

def search_str(lengthy_str, search_word):
    for char_search_word in search_word:
        print("character\"%s\":"%char_search_word,end="")
        no_of_occ = 0
        list_index = []
        dict= {}
        for index, char_lengthy_str in enumerate(lengthy_str,1):
            if char_lengthy_str == char_search_word:
                list_index.append(index)
           #     print("(num of occ,[%s]," % index, end="")
                no_of_occ += 1
        print(list_index)
        print(":no of occ \"%s\"\n"%no_of_occ)
    return dict
search_str(lengthy_str,search_word)
# -*- coding: utf-8 -*-

from selenium import webdriver
import time

class Bot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver')

    def SendMessage(self):
        self.driver.get('https://www.promobank.com.br/')
        


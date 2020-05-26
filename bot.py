# -*- coding: utf-8 -*-

from selenium import webdriver
import time

class Bot:
    def __init__(self):
        nEmpresa = 2710
        nLogin = 
        options = 
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver')

    def Login(self):
        driver.get("https://www.promobank.com.br")
        time.sleep(30)
        iframe = driver.find_element(By.CSS_SELECTOR, "placeholder="Código da empresa" > Empresa")
        driver.switch_to.frame(Empresa)
        imput.send_keys(nEmpresa)
        iframe = driver.find_element(By.CSS_SELECTOR, "placeholder="Seu login" > Login")
        driver.switch_to.frame(Login)
        imput.send_keys(nLogin)

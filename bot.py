# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Bot:
    def __init__(self):
        self.codigo_empresa = "codigo"
        self.login = "login"
        self.senha = "senha"

        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def Login(self):
        self.driver.get('https://www.promobank.com.br')
        time.sleep(5)

        emp_senha_element = self.driver.find_element(By.ID, "loginEmpresa")
        time.sleep(5)
        emp_senha_element.send_keys(self.codigo_empresa)
        time.sleep(5)

        usu_login_element = self.driver.find_element(By.ID, "loginUsuario")
        time.sleep(5)
        usu_login_element.send_keys(self.login)
        time.sleep(5)

        usu_senha_element = self.driver.find_element(By.ID, "loginSenha")
        time.sleep(5)
        usu_senha_element.send_keys(self.senha)
        time.sleep(5)

        self.driver.find_element(By.ID, "submitButton").click()
        time.sleep(5)


bot = Bot()
bot.Login()

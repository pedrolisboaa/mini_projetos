from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
import openpyxl

formulario = 'https://docs.google.com/forms/d/e/1FAIpQLScYAQmg4pLdzW9Qqm_M4KPpbGEakOSdP2ZZ1ZW0G3PAAnXZFg/viewform'

tabela = pd.read_excel('dados.xlsx')
for i, cpf in enumerate(tabela['CPF']):
    email = tabela.loc[i, 'Email']
    descricao = tabela.loc[i, 'Descricão']
    valor = tabela.loc[i, 'Valor']

    driver = webdriver.Chrome()
    driver.get(formulario)
    sleep(1)
    # cpf
    driver.find_element(By.XPATH,
                        '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(
        cpf)
    # email
    driver.find_element(By.XPATH,
                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(
        email)
    # descrição
    driver.find_element(By.XPATH,
                        '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys(
        descricao)
    # valor
    driver.find_element(By.XPATH,
                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(
        valor)
    # enviar
    driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span').click()
    # fechar navegador
    sleep(1)

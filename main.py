from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

imagem = os.path.abspath("download.jpeg")
mensagem = "mensagem teste, por favor, ignorar";
numero = "21966004286"
nome = "fulano"

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# primeira função: setup das coisas
driver.get("https://web.whatsapp.com/") # abre a página


# segunda função: lançamento de fato

WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/button/div[2]/span'))) # espera até a parte de pesquisa aparecer

time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/button/div[2]/span').click() # clica no elemento

time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p').send_keys(numero) # digita o número no campo

time.sleep(5)

WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="pane-side"]/div/div/div/div[2]'))) # espera até o primeiro item ficar visível

time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="pane-side"]/div/div/div/div[2]').click() # clica no primeiro item da lista

WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[1]/div/button'))) # espera a barra de + aparecer

driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[1]/div/button').click() # clica na barra de + 

image_upload = driver.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]') # coloca a imagem pra enviar

image_upload.send_keys(imagem) # de fato envia a mensagem

WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[2]/span/div/div/div/div[2]/div/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/p'))) # espera a barra de mensagem aparecer

driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[2]/span/div/div/div/div[2]/div/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/p').send_keys(mensagem); # escreve a mensagem de texto

driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[2]/span/div/div/div/div[2]/div/div[2]/div[2]/div/div').click(); # escreve a mensagem de texto

driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/span/button/span').click() # clica no botão de esquecer as coisas

# continua usando as funções de escolha
time.sleep(600)



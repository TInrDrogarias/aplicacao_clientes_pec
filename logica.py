# Importando todas as bibliotecas
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk
from tkinter import filedialog, messagebox
import csv
import time
import os


# declarando as variáveis que vão ser usadas por todos as funções
service = Service(ChromeDriverManager().install())
numero = []
contato = []
texto = ""

# Importa a imagem para o programa
def importar_imagem():
    imagem = filedialog.askopenfilename(title="Escolha um arquivo", filetypes=[("Todos os Arquivos", "*.*")])
    imagem = os.path.abspath(imagem)
    messagebox.showinfo("Aviso!", "A imagem foi importada pelo programa!")
    print(imagem)
    return imagem

# Importa os contatos do arquivo CSV
def importar_contatos():
    arquivo_csv = filedialog.askopenfilename(title="Escolha um arquivo csv a ser importado", filetypes=[("Somente .csv", "*.csv*")])
    with open(arquivo_csv, mode='r') as file_csv:
        arquivo_contato = csv.reader(file_csv)
        for linhas in arquivo_contato:
            a = linhas[0]
            b = a.split(";")
            contato.append(b[0])
            numero.append(b[1])
            print(numero, contato)
    numero.pop(0)
    contato.pop(0)
    return numero, contato

# Insere um texto padrão
def inserir_texto():
    return "Teste"

# Processo de envio da mensagem
def processo(contato, mensagem, numero, imagem):
    driver = webdriver.Chrome(service=service)
    driver.get("https://web.whatsapp.com/")
    time.sleep(20)
    
    for x in range(len(numero) + 1):
        search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]') # encontra o elemento na caixa de procura
        search_box.click() # clica na caixa de procura
        search_box.send_keys(numero[x]) # digita a mensagem
        time.sleep(2) # espera por um momento
        acha_contato = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='pane-side']//div[2]")))  # encontra o primeiro item da lista de contatos
        acha_contato.click() # clica no primeiro item
        time.sleep(2) # espera por um momento
        driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[1]/div/button').click() # clica na barra de + 
        time.sleep(2)
        image_upload = driver.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]') # coloca a imagem pra enviar
        time.sleep(2)
        image_upload.send_keys(imagem) # de fato envia a imagem
        time.sleep(2)
        WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]//p'))) # espera a barra de mensagem aparecer
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="app"]//p').send_keys(f"mensagem"); # escreve a mensagem de texto
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[2]/span/div/div/div/div[2]/div/div[2]/div[2]/div/div').click(); # clica para enviar
        search_box.click()
        search_box.clear()
        time.sleep(5)

"""
imagem = importar_imagem()
numero, contato = importar_contatos()
texto = inserir_texto()
processo(contato, texto, numero, imagem)
"""
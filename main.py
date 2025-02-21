# importando todas as bibliotecas necessárias
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
import csv
import time
import os

service = Service(ChromeDriverManager().install())

numero = []
contato = []
x = 0;
texto = ""

# criando a interface da aplicação
root = Tk();
root.title("PEC - Aplicação");
root.geometry("720x480");
root.resizable(height="false", width="false");

# definindo as funções de configuração
def importar_imagem():
	imagem = filedialog.askopenfilename(title="Escolha um arquivo", filetypes=[("Todos os Arquivos", "*.*")])
	imagem = os.path.abspath(imagem)
	messagebox.showinfo("Aviso!", "A imagem foi importada pelo programa!")
	print(imagem)
	return imagem

def importar_contatos():
	arquivo_csv = filedialog.askopenfilename(title="Escolha um arquivo csv a ser importado", filetypes=[("Somente .csv", "*.csv*")])
	with open(arquivo_csv, mode = 'r') as file_csv:
		arquivo_contato = csv.reader(file_csv)
		x = 0;
		for linhas in arquivo_contato:
			a = linhas[0]
			b = a.split(";")
			contato.append(b[0])
			numero.append(b[1])
			print(numero, contato)
	numero.pop(0)
	contato.pop(0)
	print(numero, contato)

def inserir_texto():
	texto = caixa_texto.get("1.0", tk.END)
	print(texto)

def processo():
	# importa o arquivo csv
	arquivo_csv = filedialog.askopenfilename(title="Escolha um arquivo csv a ser importado", filetypes=[("Somente .csv", "*.csv*")])
	with open(arquivo_csv, mode = 'r') as file_csv:
		arquivo_contato = csv.reader(file_csv)
		x = 0;
		for linhas in arquivo_contato:
			a = linhas[0]
			b = a.split(";")
			contato.append(b[0])
			numero.append(b[1])
			print(numero, contato)
	numero.pop(0)
	contato.pop(0)
	print(numero, contato)

	# importa a imagem
	imagem = filedialog.askopenfilename(title="Escolha um arquivo de imagem", filetypes=[("Todos os Arquivos", "*.*")])
	imagem = os.path.abspath(imagem)
	messagebox.showinfo("Aviso!", "A imagem foi importada pelo programa!")
	print(imagem)
	return imagem

	texto = simpledialog.askstring("Digite a mensagem ao usuário", "")

	driver = webdriver.Chrome(service=service)
	driver.get("https://web.whatsapp.com/")
	x = 0;
	while x < len(numero):
		WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/button/div[2]/span'))) # espera até a parte de pesquisa aparecer
		time.sleep(2)
		driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/button/div[2]/span').click() # clica no elemento
		time.sleep(2)
		driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p').send_keys(numero[x]) # digita o número no campo
		time.sleep(2)
		WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="pane-side"]/div/div/div/div[2]'))) # espera até o primeiro item ficar visível
		time.sleep(2)
		driver.find_element(By.XPATH, '//*[@id="pane-side"]/div/div/div/div[2]').click() # clica no primeiro item da lista
		time.sleep(2)
		WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[1]/div/button'))) # espera a barra de + aparecer
		time.sleep(2)
		driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[1]/div/button').click() # clica na barra de + 
		time.sleep(2)
		image_upload = driver.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]') # coloca a imagem pra enviar
		time.sleep(2)
		image_upload.send_keys(imagem) # de fato envia a mensagem
		time.sleep(2)
		WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[2]/span/div/div/div/div[2]/div/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/p'))) # espera a barra de mensagem aparecer
		time.sleep(2)
		driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[2]/span/div/div/div/div[2]/div/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/p').send_keys(f"{contato}, {mensagem}"); # escreve a mensagem de texto
		time.sleep(2)
		driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[2]/span/div/div/div/div[2]/div/div[2]/div[2]/div/div').click(); # escreve a mensagem de texto
		time.sleep(2)
		driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/span/button/span').click() # clica no botão de esquecer as coisas
		x += 1;

# criando os botões e os posicionando
importar_contatos =  tk.Button(root, text="importar contatos", command=importar_contatos)
importar_contatos.place(x=260, y=120)

importar_imagem = tk.Button(root, text="inserir imagem", command=importar_imagem)
importar_imagem.place(x=520, y=120)

caixa_texto = tk.Text(root, height=5, width=25)
caixa_texto.place(x=220, y=260)

inserir_mensagem = tk.Button(root, text="inserir mensagem", command=inserir_texto)
inserir_mensagem.place(x=260, y=360)

iniciar_processo =  tk.Button(root, text="iniciar processo", command=processo)
iniciar_processo.place(x=40, y=120)

cancelar_processo =  tk.Button(root, text="encerrar processo")
cancelar_processo.place(x=40, y=240)






root.mainloop()
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
import csv

root = Tk();
root.title("PEC - Aplicação");
root.geometry("720x480");
root.resizable(height="false", width="false");

# definindo as funções de configuração
def importar_imagem():
	imagem = filedialog.askopenfilename(title="Escolha um arquivo", filetypes=[("Todos os Arquivos", "*.*")])
	messagebox.showinfo("Aviso!", "A imagem foi importada pelo programa!")
	print(imagem)
	return imagem

def importar_contatos():
		numero = []
		contato = []
		arquivo_csv = filedialog.askopenfilename(title="Escolha um arquivo csv a ser importado", filetypes=[("Somente .csv", "*.csv*")])
		with open(arquivo_csv, mode = 'r') as file_csv:
			arquivo_contato = csv.reader(file_csv)
			x = 0;
			for linhas in arquivo_contato:
				a = linhas[0]
				b = a.split(";")
				numero.append(b[0])
				contato.append(b[1])
				print(numero, contato)
		return numero, contato

def inserir_texto():
	texto = caixa_texto.get("1.0", tk.END)
	print(texto)
	return texto

def iniciar_processo():
	setup_web()
	enviar_mensagem()

def setup_web():
	service = Service(ChromeDriverManager().install())
	driver = webdriver.Chrome(service=service)
	driver.get("https://web.whatsapp.com/") # abre a página
	timer.sleep(7200)

def envio_mensagem(imagem, numero, contato, texto): # segunda função: lançamento de fato
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

	image_upload.send_keys(imagem) # de fato envia a imagem

	WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[2]/span/div/div/div/div[2]/div/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/p'))) # espera a barra de mensagem aparecer

	driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[2]/span/div/div/div/div[2]/div/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/p').send_keys(texto); # escreve a mensagem de texto

	driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[2]/span/div/div/div/div[2]/div/div[2]/div[2]/div/div').click(); # escreve a mensagem de texto

	driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/span/button/span').click() # clica no botão de esquecer as coisas




# criando os botões e os posicionando
importar_contatos =  tk.Button(root, text="importar contatos", command=importar_contatos)
importar_contatos.place(x=260, y=120)

importar_imagem = tk.Button(root, text="inserir imagem", command=importar_imagem)
importar_imagem.place(x=520, y=120)

caixa_texto = tk.Text(root, height=5, width=25)
caixa_texto.place(x=220, y=260)

inserir_mensagem = tk.Button(root, text="inserir mensagem", command=inserir_texto)
inserir_mensagem.place(x=260, y=360)

iniciar_processo =  tk.Button(root, text="iniciar processo", command=iniciar_processo)
iniciar_processo.place(x=40, y=120)

cancelar_processo =  tk.Button(root, text="encerrar processo", command=encerrar_processo)
cancelar_processo.place(x=40, y=240)






root.mainloop()
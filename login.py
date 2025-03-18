import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import hashlib
import os
from PIL import Image, ImageTk

# Simulação de credenciais
USERNAME = "admin"
PASSWORD = "1234"

# Função para hash da senha
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# Função para autenticação
def authenticate(username, password):
    return username == USERNAME and hash_password(password) == hash_password(PASSWORD)

# Função para sair
def sair():
    root1.destroy()  # Fecha a janela principal

# Função para abrir a janela principal
def open_main_application():
    global bg  # Mantém a referência ativa

    root1 = tk.Tk()
    root1.geometry("720x480")
    root1.title("Aplicação: PEC")

    # Carregar imagem de fundo corretamente
    bg = PhotoImage(file="background_2.png")
    label1 = tk.Label(root1, image=bg)
    label1.place(x=0, y=0)

    # Criando os botões corretamente
    importar_imagem = tk.Button(root1, text="Importar imagem", height=14, width=26, bg="#283051", fg="#FFD700")
    importar_imagem.place(x=260, y=40)

    importar_contatos = tk.Button(root1, text="Importar contatos", height=14, width=26, bg="#283051", fg="#FFD700")
    importar_contatos.place(x=470, y=40)

    adicionar_mensagem = tk.Button(root1, text="Adicionar mensagem", height=14, width=26, bg="#283051", fg="#FFD700")
    adicionar_mensagem.place(x=260, y=250)

    sair_button = tk.Button(root1, text="Sair", height=2, width=20, bg="#F5F6F5", command=sair)
    sair_button.place(x=30, y=200)

    iniciar_processo = tk.Button(root1, text="Iniciar envio", height=14, width=26, bg="#283051", fg="#FFD700")
    iniciar_processo.place(x=470, y=250)

    root1.mainloop()

# Função para login
def login():
    username = username_var.get()
    password = password_var.get()

    if authenticate(username, password):
        root.destroy()  # Fecha a janela de login
        open_main_application()
    else:
        print("Login falhou")

# Criando a janela de login
root = tk.Tk()
root.title("Login / Registro")
root.geometry("750x400")
root.resizable(False, False)

# Carregamento da imagem de fundo corretamente
bg_image = Image.open("background.png").resize((750, 400))
bg_photo = ImageTk.PhotoImage(bg_image)

background_label = tk.Label(root, image=bg_photo)
background_label.place(relwidth=1, relheight=1)

# Frame para o conteúdo
content_frame = tk.Frame(root, bg="")
content_frame.place(relx=0.05, rely=0.5, anchor='w')

# Variáveis para armazenar dados
username_var = tk.StringVar()
password_var = tk.StringVar()

# Layout de entrada
ttk.Label(content_frame, text="Usuário:").pack(pady=10, anchor='w')
username_entry = ttk.Entry(content_frame, textvariable=username_var)
username_entry.pack(pady=5, anchor='w')

ttk.Label(content_frame, text="Senha:").pack(pady=10, anchor='w')
password_entry = ttk.Entry(content_frame, textvariable=password_var, show="*")
password_entry.pack(pady=5, anchor='w')

# Botão de login
login_button = ttk.Button(content_frame, text="Login", command=login)
login_button.pack(pady=20, anchor='w')

root.mainloop()

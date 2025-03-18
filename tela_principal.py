import tkinter as tk
import tkinter as ttk
from tkinter import *

def pegar_mensagem():
    mensagem = caixa_texto.get("1.0", 'end-1c')
    return mensagem

root = tk.Tk() # criando uma janela principal
root.geometry("750x400")
root.title("Aplicação: PEC")
root.minsize(720, 480)
root.maxsize(720, 480)

bg = PhotoImage(file = "background_2.png")
label1 = Label(root, image = bg)
label1.place(x = 0, y = 0)

def sair():
    quit()


importar_imagem = ttk.Button(root, text="Importar imagem", height=14, width=28, bg="#283051", fg="#FFD700", borderwidth=0)
importar_imagem.configure(font=('Sans', '8', 'bold'))
importar_imagem.place(x=260, y=40)

importar_contatos = ttk.Button(root, text="Importar contatos", height=14, width=28, bg="#283051", fg="#FFD700", borderwidth=0)
importar_contatos.configure(font=('Sans', '8', 'bold'))
importar_contatos.place(x=470, y=40)

adicionar_mensagem = ttk.Button(root, text="Adicionar mensagem", height=14, width=28, bg="#283051", fg="#FFD700", borderwidth=0)
adicionar_mensagem.configure(font=('Sans', '8', 'bold'))
adicionar_mensagem.place(x=260, y=250)

sair = ttk.Button(root, text="Sair", height=5, width=20, bg="#F5F6F5", borderwidth=0, command=sair)
sair.configure(font=('Sans', '10', 'bold'))
sair.place(x=30, y=200)

iniciar_processo = ttk.Button(root, text="Iniciar envio", height=14, width=28,  bg="#283051", fg="#FFD700", borderwidth=0)
iniciar_processo.configure(font=("Sans", "8", "bold"))
iniciar_processo.place(x=470, y=250)

root.mainloop()
import tkinter as tk
from tkinter import ttk, font, messagebox
from tkinter import PhotoImage

#criando janela do app
janela = tk.Tk()
janela.title("Bloco de notas")

#pode mudar a cor de fundo de acordo com a que vc quiser
janela.configure(bg="#000000")
janela.geometry("600x400")

fonte_nome = font.Font(family="Times New Roman", size=24, weight="bold")
rotulo_nome = tk.Label(janela, text="Meu Bloco de Notas",  font=fonte_nome, bg="#000000", fg="#FFFFFF").pack(pady=20)

frame = tk.Frame(janela, bg="#808080").pack(pady=10)

entrada_tarefa = tk.Entry(frame, font=("Times New Roman", 14), relief=tk.FLAT, bg="white", fg="black", width=28)
entrada_tarefa.pack(side=tk.LEFT, padx=60, pady=5)

botao_adicionar = tk.Button(frame, text="Adicionar tarefa", bg="#008000", fg="white", height=1, width=15, font=("Roboto", 11), relief=tk.FLAT)
botao_adicionar.pack(side=tk.LEFT, padx=2)

janela.mainloop()
import tkinter as tk
from tkinter import ttk, font, messagebox
from tkinter import PhotoImage

#criando janela do app
janela = tk.Tk()
janela.title("Bloco de notas")
janela.configure(bg="#FFFFFF")
janela.geometry("600x400")

frame_edicao = None

#funcao de adicionar as tarefas
def adicionar():
    global frame_edicao
    tarefa = entrada_tarefa.get().strip()
    if tarefa and tarefa != "Digite sua atividade":
        if frame_edicao is not None:
            atualizar_tarefa(tarefa)
            frame_edicao = None
        else:
            criar_tarefa(tarefa)
            entrada_tarefa.delete(0, tk.END)
    else:
        messagebox.showwarning("Por favor insira uma atividade!")

#funcao para criar uma tarefa
def criar_tarefa(tarefa):
    frame_tarefa = tk.Frame(canva2, bg="white", bd=1, relief=tk.SOLID)

    label_tarefa = tk.Label(frame_tarefa, text=tarefa, font=("Times New Roman", 16), bg="white", width=15, height=1, anchor="w")
    label_tarefa.pack(side=tk.LEFT, fill=tk.X, padx=10, pady=5)

    botao_editar = tk.Button(frame_tarefa, image=icon_editar, command=lambda f=frame_tarefa, l=label_tarefa: preparar_edicao(f, l), bg='white', width=25, relief=tk.FLAT)
    botao_editar.pack(side=tk.RIGHT, padx=5)

    botao_deletar = tk.Button(frame_tarefa, image=icon_deletar, command=lambda f=frame_tarefa: deletar_tarefa(f), bg='white', width=25, relief=tk.FLAT)
    botao_deletar.pack(side=tk.RIGHT, padx=5)

    frame_tarefa.pack(fill=tk.X, padx=125, pady=5)

    checkbutton = ttk.Checkbutton(frame_tarefa, command=lambda label=label_tarefa: alterar_sublinhado(label))
    checkbutton.pack(side=tk.RIGHT, padx=5)

    canva2.update_idletasks()
    canva.config(scrollregion=canva.bbox("all"))

def preparar_edicao(frame_tarefa, label_tarefa):
    global frame_edicao
    frame_edicao = frame_tarefa
    entrada_tarefa.delete(0, tk.END)
    entrada_tarefa.insert(0, label_tarefa.cget("text"))

def atualizar_tarefa(nova_tarefa):
    global frame_edicao
    for widget in frame_edicao.winfo_children():
        if isinstance(widget, tk.Label):
            widget.config(text=nova_tarefa)

def deletar_tarefa(frame_tarefa):
    frame_tarefa.destroy()
    canva2.update_idletasks()
    canva.config(scrollregion=canva2.bbox("all"))

def alterar_sublinhado(label):
    fonte_atual = label.cget("font")
    if "overstrike" in fonte_atual:
        nova_fonte = fonte_atual.replace(" overstrike", "")
    else:
        nova_fonte = fonte_atual + " overstrike"
    label.config(font=nova_fonte)

icon_editar = PhotoImage(file="edit.png").subsample(50, 50)
icon_deletar = PhotoImage(file="clear.png").subsample(60, 60)

fonte_nome = font.Font(family="Times New Roman", size=24, weight="bold")
rotulo_nome = tk.Label(janela, text="Meu Bloco de Notas", font=fonte_nome, bg="#FFFFFF", fg="#000000")
rotulo_nome.pack(pady=20)

frame = tk.Frame(janela, bg="#F0F0F0")
frame.pack(pady=20)

entrada_tarefa = tk.Entry(frame, font=("Times New Roman", 14), relief=tk.FLAT, bg="white", fg="black", width=28)
entrada_tarefa.pack(side=tk.LEFT, padx=60, pady=5)

botao_adicionar = tk.Button(frame, command=adicionar, text="Adicionar tarefa", bg="#008000", fg="white", height=1, width=15, font=("Roboto", 11), relief=tk.FLAT)
botao_adicionar.pack(side=tk.LEFT, padx=2)

#criando frame para adicionar as tarefas 
frame_lista = tk.Frame(janela, bg="white")
frame_lista.pack(fill="both", expand=True, padx=10, pady=10)

canva = tk.Canvas(frame_lista, bg="white")
canva.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scroll = ttk.Scrollbar(frame_lista, orient="vertical", command=canva.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

canva.configure(yscrollcommand=scroll.set)
canva2 = tk.Frame(canva, bg="white")
canva.create_window((0, 0), window=canva2, anchor="nw")
canva2.bind("<Configure>", lambda e: canva.configure(scrollregion=canva.bbox("all")))

janela.mainloop()

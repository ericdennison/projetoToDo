import tkinter as tk
from tkinter import ttk, font, messagebox
from tkinter import PhotoImage


# JANELA inicio
janela = tk.Tk()
janela.title("Meu app de Tarefas")
janela.configure(bg='#F0F0F0')
janela.geometry('500x600')

# Cabeçalho
fonte_cabecalho = font.Font(family='Garamond', size=24, weight='bold')
rotulo_cabecalho = tk.Label(janela,text="Meu App de Tarefas", font=fonte_cabecalho, bg='#F0F0F0', fg='#333').pack(pady=20,)

# Container
frame = tk.Frame(janela, bg='#F0F0F0').pack(pady=10)

# Campo Entrada Texto
entrada_tarefa = tk.Entry(frame, font=('Garamond', 14), relief=tk.FLAT, bg='white', fg='grey', width=30)
entrada_tarefa.pack(side=tk.LEFT, padx=10)

# Botão
botao_adicionar = tk.Button(frame, text="Adicionar Tarefa", bg='#4CAF50', fg='white', height=1, width=15, font=('Roboto',11), relief=tk.FLAT)
botao_adicionar.pack(side=tk.LEFT, padx=10)

janela.mainloop()
# JANELA fim
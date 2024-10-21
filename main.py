import tkinter as tk
from tkinter import ttk, font, messagebox
from tkinter import PhotoImage


# JANELA inicio
janela = tk.Tk()
janela.title("Meu app de Tarefas")
janela.configure(bg='#F0F0F0')
janela.geometry('550x600')

frame_em_edicao = None

# Função Adicionar Tarefa
def adicionar_tarefa():
    global frame_em_edicao
    
    tarefa = entrada_tarefa.get().strip()
    if tarefa and tarefa != "Escreva sua tarefa aqui":
        if frame_em_edicao is not None:
            atualizar_tarefa(tarefa)
            frame_em_edicao = None
        else:
            adicionar_item_tarefa(tarefa)
            entrada_tarefa.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada Inválida", "Por favor Insira uma tarefa!")




# Cabeçalho
fonte_cabecalho = font.Font(family='Garamond', size=24, weight='bold')
rotulo_cabecalho = tk.Label(janela,text="Meu App de Tarefas", font=fonte_cabecalho, bg='#F0F0F0', fg='#333').pack(pady=20,)

# Container
frame = tk.Frame(janela, bg='#F0F0F0')
frame.pack(pady=10)

# Campo Entrada Texto
entrada_tarefa = tk.Entry(frame, font=('Garamond', 14), relief=tk.FLAT, bg='white', fg='grey', width=30)
entrada_tarefa.pack(side=tk.LEFT, padx=10)

# Botão
botao_adicionar = tk.Button(frame, text="Adicionar Tarefa", bg='#4CAF50', fg='white', height=1, width=15, font=('Roboto',11), relief=tk.FLAT)
botao_adicionar.pack(side=tk.LEFT, padx=10)

# Criar frame lista_tarefas rolagem
frame_lista_tarefas = tk.Frame(janela, bg="White")
frame_lista_tarefas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

canvas = tk.Canvas(frame_lista_tarefas, bg='white')
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#Scrollbar
scrollbar = ttk.Scrollbar(frame_lista_tarefas, orient='vertical', command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas_interior = tk.Frame(canvas, bg='white')
canvas.create_window((0,0), window=canvas_interior, anchor='nw')
canvas_interior.bind('<Configure>',lambda e: canvas.configure(scrollregion=canvas.bbox('all')))



janela.mainloop()
# JANELA fim
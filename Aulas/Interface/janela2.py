import tkinter as tk
from tkinter import messagebox

def mostrar_saudacao():
    # Obtem o nome inserido pelo usuario
    nome = entrada_nome.get()
    if nome:
        # Exibe uma mensagem de saudacao
        messagebox.showinfo("Saudação", f"Olá , {nome}!")
    else:
        # Aviso caso de erro
        messagebox.showwarning("Atenção!", "Por favor, insira seu nome!")

# Cria janela
janela = tk.Tk()
janela.title("Aplicativo de Saudação")
janela.geometry("400x300")

# Cria um rótulo
rotulo = tk.Label(janela, text="Insira seu nome:", font=("Arial", 14))
rotulo.pack(pady=10)

# Cria um campo de entrada
entrada_nome = tk.Entry(janela, font=("Arial", 14))
entrada_nome.pack(pady=10)

# Cria um botão
botao = tk.Button(janela, text="Saudar", command=mostrar_saudacao, font=("Arial", 14))
botao.pack(pady=20)

# Inicia código
janela.mainloop()
import tkinter as tk

janela = tk.Tk()

janela.title("Titulo da aba")
janela.geometry("400x300")

rotulo = tk.Label(janela, text="Olá, TKinter")
rotulo.pack(pady=10)

botao = tk.Button(janela, text="Clique aqui", command=janela.quit)
botao.pack(pady=10)

janela.mainloop()
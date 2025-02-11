import tkinter as tk

# Função para atualizar visor com os numeros e operacoes

def press(Key):
    current = visor.get()
    visor.set(current + str(Key))

# Função para calcular o resultado
def calcular():
    try:
        result = eval(visor.get())
        visor.set(result)
    except Exception as e:
        visor.set("Erro")

# Função para limpar o visor
def limpar():
    visor.set("")

# Criando janela principal
root = tk.Tk()
root.title("Calculadora")

# Definindo o visor da calculadora
visor = tk.StringVar()
entry = tk.Entry(root, textvariable= visor, font= ("Arial", 20), bd= 10, relief= "sunken", width= 16, justify= "right")
entry.grid(row= 0, column= 0, columnspan= 4)

# Definindo os botoes
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Adicionando os botoes a janela
for(text, row, col) in buttons:
    if text == '=':
        buttons = tk.Button(root, text= text, font=("Arial", 20), width= 5, height= 2, command= calcular)
    elif text == 'C':
        buttons = tk.Button(root, text= text, font=("Arial", 20), width= 5, height= 2, command= limpar)
    else:
        buttons = tk.Button(root, text= text, font=("Arial", 20), width= 5, height= 2, command= lambda key = text: press(key))
    buttons.grid(row= row, column= col)

# Iniciar a interface gráfica
root.mainloop()
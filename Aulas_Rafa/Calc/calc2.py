import tkinter as tk
import math

# Função para atualizar visor com os números e operações
def press(Key):
    current = visor.get()
    # Verificar se o ponto já foi adicionado no número atual
    if Key == '.' and '.' not in current.split('+-*/^')[::-1][0]:  # Verifica se o ponto já está no número
        visor.set(current + str(Key))
    elif Key != '.':
        visor.set(current + str(Key))

# Função para calcular o resultado
def calcular():
    try:
        # Substituir o '^' por '**' para operação de exponenciação
        expression = visor.get().replace('^', '**')
        result = eval(expression)
        visor.set(result)
    except Exception as e:
        visor.set("Erro")

# Função para calcular a raiz quadrada
def raiz_quadrada():
    try:
        current = float(visor.get())
        result = math.sqrt(current)
        visor.set(result)
    except Exception as e:
        visor.set("Erro")

# Função para limpar o visor
def limpar():
    visor.set("")

# Função para apagar o último caractere (backspace)
def backspace():
    current = visor.get()
    visor.set(current[:-1])

# Criando janela principal
root = tk.Tk()
root.title("Calculadora")

# Definindo o visor da calculadora
visor = tk.StringVar()
entry = tk.Entry(root, textvariable=visor, font=("Arial", 20), bd=10, relief="sunken", width=16, justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Definindo os botões
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('←', 4, 2), ('+', 4, 3),
    ('.', 5, 0), ('^', 5, 1), ('√', 5, 2), ('=', 5, 3),  # Exponenciação, Raiz e Backspace
]

# Adicionando os botões à janela
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, font=("Arial", 20), width=5, height=2, command=calcular)
    elif text == 'C':
        button = tk.Button(root, text=text, font=("Arial", 20), width=5, height=2, command=limpar)
    elif text == '√':
        button = tk.Button(root, text=text, font=("Arial", 20), width=5, height=2, command=raiz_quadrada)
    elif text == '←':
        button = tk.Button(root, text=text, font=("Arial", 20), width=5, height=2, command=backspace)
    else:
        button = tk.Button(root, text=text, font=("Arial", 20), width=5, height=2, command=lambda key=text: press(key))
    button.grid(row=row, column=col)

# Iniciar a interface gráfica
root.mainloop()

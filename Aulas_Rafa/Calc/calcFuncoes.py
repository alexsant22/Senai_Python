import tkinter as tk

# Função para somar dois números
def somar():
    try:
        valor1 = float(entry_valor1.get()) # Pega o valor1
        valor2 = float(entry_valor2.get()) # Pega o valor2
        resultado = valor1 + valor2
        label_resultado.config(text = f"Resultado: {resultado}")
    except ValueError:
        label_resultado.config(text = "Por favor, Insira números válidos")

# Configuração da Janela
root = tk.Tk()
root.title("Calculadora")

# Labels
label_valor1 = tk.Label(root, text="Valor 1", font=("Arial", 14))
label_valor1.grid(row=0, column= 0, padx= 10, pady= 10)

label_valor2 = tk.Label(root, text="Valor 2", font=("Arial", 14))
label_valor2.grid(row= 1, column= 0, padx= 10, pady= 10)

# Entradas
entry_valor1 = tk.Entry(root, font=("Arial", 14))
entry_valor1.grid(row= 0, column= 1, padx= 10, pady= 10)

entry_valor2 = tk.Entry(root, font=("Arial", 14))
entry_valor2.grid(row= 1, column= 1, padx= 10, pady= 10)

# Botão somar
botao_somar = tk.Button(root, text="Somar", font=("Arial", 14), command= somar)
botao_somar.grid(row= 2, column= 0, columnspan= 2, pady= 10)

# Label para exibir o resultado
label_resultado = tk.Label(root, text="Resultado", font=("Arial", 14))
label_resultado.grid(row= 3, column= 0, columnspan= 2, pady= 10)

# Inicia a interface grafica
root.mainloop()
import tkinter as tk
import requests

def obter_cotacao():
    try:
        url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
        resposta = requests.get(url)
        dados = resposta.json()
        return float(dados["USDBRL"]["bid"])
    except Exception:
        return None

def converter():
    try:
        valor = float(entrada_valor.get())
        cotacao_dolar = obter_cotacao()
        
        if cotacao_dolar is None:
            resultado.config(text="Erro ao acessar a API.")
            return
        
        if opcao.get() == "BRL → USD":
            valor_convertido = valor / cotacao_dolar
            resultado.config(text=f"USD: ${valor_convertido:.2f}")
        else:
            valor_convertido = valor * cotacao_dolar
            resultado.config(text=f"BRL: R${valor_convertido:.2f}")
    except ValueError:
        resultado.config(text="Por favor, insira um número válido.")

# Configuração da interface Tkinter
janela = tk.Tk()
janela.title("Conversor de Moeda")

# Campo de entrada
tk.Label(janela, text="Valor:", font=("Arial", 12)).pack(padx=10, pady=5)
entrada_valor = tk.Entry(janela, font=("Arial", 12))
entrada_valor.pack(padx=10, pady=5)

# Opções de conversão
opcao = tk.StringVar(value="BRL → USD")
tk.Radiobutton(janela, text="BRL → USD", variable=opcao, value="BRL → USD", font=("Arial", 12)).pack()
tk.Radiobutton(janela, text="USD → BRL", variable=opcao, value="USD → BRL", font=("Arial", 12)).pack()

# Botão de conversão
botao_converter = tk.Button(janela, text="Converter", command=converter, font=("Arial", 12))
botao_converter.pack(padx=10, pady=10)

# Rótulo do resultado
resultado = tk.Label(janela, text="Resultado: 0.00", font=("Arial", 14, "bold"))
resultado.pack(padx=10, pady=10)

# Executa a interface gráfica
janela.mainloop()

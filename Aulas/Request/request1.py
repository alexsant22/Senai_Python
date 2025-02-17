import requests

url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

response = requests.get(url)

dados = response.json()

#print(dados["USDBRL"]["bid"])

dolar = float(dados["USDBRL"]["bid"])

real = float(input("Digite o valor em doláres: "))
resultado = real * dolar

print(f"O valor {real} USD fica: {resultado} BRL")
import requests

urlDolar = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
urlReal = "https://economia.awesomeapi.com.br/json/last/BRL-USD"

responseDolar = requests.get(urlDolar)
responseReal = requests.get(urlReal)

dadosDolar = responseDolar.json()
dadosReal = responseReal.json()

dolar = float(dadosDolar["USDBRL"]["bid"])
real = float(dadosReal["BRLUSD"]["bid"])

escolha = int(input("Digite 1 para converter Dolar para Real\nDigite 2 para converter Real para dolar:\n"))

match escolha:
    case 1:
        inputUser = float(input("Digite o valor em doláres: "))
        resultado = inputUser * dolar
        print(f"O valor {inputUser} USD fica: {resultado} BRL")
    case 2:
        inputUser = float(input("Digite o valor em reais: "))
        resultado = inputUser * real
        print(f"O valor {inputUser} BRL fica: {resultado} USD")
    case _:
        print("Opção inválida.")
import requests

bitcoinBRL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=brl"
bitcoinUSD = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

responseBRL = requests.get(bitcoinBRL)
responseUSD = requests.get(bitcoinUSD)

dadosBRL = responseBRL.json()
dadosUSD = responseUSD.json()

real = float(dadosBRL["bitcoin"]["brl"])
dolar = float(dadosUSD["bitcoin"]["usd"])

escolha = int(input("Digite 1 para Bitcoin para Real\nDigite 2 para Bitcoin para Dolar:\n"))

match escolha:
    case 1:
        user = float(input("Digite em reais: "))
        resultado = user * real
        print(f'Valor do bitcoin: {resultado}')
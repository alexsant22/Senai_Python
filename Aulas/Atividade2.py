#constantes
VALOR_KWH = 0.75 #Valor quilowatt-hora
TAXA_FIXA = 20 #Taxa fixa mensal

#entradas
nome = input("Digite seu nome: ")
consumo_mensal = float(input("Digite seu consumo mensal em kWh: "))

#variaveis de desconto
DESCONTO = 0.1 #desconto de 10%

#regras para desconto
if consumo_mensal < 100:
    desc = consumo_mensal - (consumo_mensal * DESCONTO)
    #consumo_total = consumo_mensal * VALOR_KWH + TAXA_FIXA - (consumo_mensal * DESCONTO)
elif 100 <= consumo_mensal <= 200:
    desc = consumo_mensal - (consumo_mensal * (DESCONTO - 0.05))
    #consumo_total = consumo_mensal * VALOR_KWH + TAXA_FIXA - (consumo_mensal * (DESCONTO - 0.05))
else:
    desc = consumo_mensal
    #consumo_total = consumo_mensal * VALOR_KWH + TAXA_FIXA

#calculo
total = desc * VALOR_KWH + TAXA_FIXA

#saidas
print(f"Cliente: {nome}\nConsumo Total em kWh: {consumo_mensal}\nValor total a pagar: {desc}")
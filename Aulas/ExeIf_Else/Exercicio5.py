nome = input("Digite seu nome: ")
valor = float(input("Qual o valor gasto no evento: "))
socio = input("Você é sócio do clube? (Digite '1' para Sim; Digite '2' para Não. )")

DESCONTO = 0.17

if socio == "1":
    valor = valor - (valor * DESCONTO)

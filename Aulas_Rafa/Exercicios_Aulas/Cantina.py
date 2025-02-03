"""
Nomes:
Alexandre Elson Costa Santana Santos - 1TDS
Carlos Gabriel Evangelista Silva - 1TDS
"""
#pedir 3 produtos
#listas
produtos = []
valor_total = []

#produtos
#NÃO USEI O WHILE
produtos.append(input("Digite o nome do produto 1: "))
q1 = int(input("Digite a quantidade do produto: "))
v1 = float(input("Digite o valor unitário do produto 1: "))
valor1 = q1 * v1
valor_total.append(valor1)

print("")
produtos.append(input("Digite o nome do produto 2: "))
q2 = int(input("Digite a quantidade do produto: "))
v2 = float(input("Digite o valor unitário do produto 2: "))
valor2 = q2 * v2
valor_total.append(valor2)

print("")
produtos.append(input("Digite o nome do produto 3: "))
q3 = int(input("Digite a quantidade do produto: "))
v3 = float(input("Digite o valor unitário do produto 3: "))
valor3 = q3 * v3
valor_total.append(valor3)

#desconto
"""
Dinheiro = 10% de desconto
Pix = 8% de desconto
Cartão = Nada de desconto
"""
DESCONTO = 0.1
total = sum(valor_total)

print("")
forma_pag = int(input("Qual a forma de pagamento:\nDinheiro digite '1'\nPix digite '2'\nCartão digite '3'\nDigite: "))
""" se quiser usar if/else
if forma_pag == 1:
    total -= (total * DESCONTO)
elif forma_pag == 2:
    total -= (total *(DESCONTO - 2))
else:
    total = total
"""
match forma_pag:
    case 1:
        total -= (total * DESCONTO)
    case 2:
        total -= (total * (DESCONTO - 2))
    case 3:
        total = total


#imprimindo resultados
print("")
print(f"Lista de produtos: {produtos}")
print(f"Valor total da sua compra: {sum(valor_total)}")
print(f"Valor da compra: {total}")
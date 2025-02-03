#pedidndo número com o tipo float usando input
num = float(input("Digite um número qualquer: "))

#montando a estrutura de verificação para saber se é um número positivo, negativo ou zero.
if num > 0: #se o número for maior que 0
    print(f"O número {num}, é positivo.")
elif num < 0: #se o número for menor que 0
    print(f"O número {num}, é negativo.")
else: #se não for nenhum dos dois acima ele é 0
    print(f"O número {num}, é igual a 0.")
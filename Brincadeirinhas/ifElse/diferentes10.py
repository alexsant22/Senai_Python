#pedindo infos
n1 = int(input("Digite um Número 1 intreiro: "))
n2 = int(input("Digite um Núnmero 2 inteiro: "))

#verificando se as duas variaveis sao iguais ou diferente
if n1 == n2:
    print("Os dois números são iguais.")
else:
    print("Os números são diferentes um do outro.")

#somando n1 + n2 e multiplicando por 2
soma = (n1 + n2)*2

#comparando resultado de soma com 10
if soma > 10:
    print("Resultado final amior do que 10.")
elif soma < 10:
    print("Resultado final menor do que 10.")
else:
    print("Resultado final igual a 10.") 
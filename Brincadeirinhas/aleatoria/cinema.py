#Cabeçário
print("Digite as seguintes informações:")
print("")

#Pedindo infos
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

#if else par valor de ingresso
if 1 >= idade <= 17:
    valor  = 15
elif idade > 17 and idade <= 64:
    valor = 30
else:
    valor = 15

#Exibindo resultados
print("")
print("Seu nome é: " + nome)
print("Valor do ingresso: R$", valor)

#pode ffazer uma condição para estudantes pagarem meia também
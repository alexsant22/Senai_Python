#Cabeçário
print("Escolha uma opção:")
print("")

#Opções
print("Digite '1' para Somar.")
print("Digite '2' para Subtrair.")
print("Digite '3' para Multiplicar.")
print("Digite '4' para dividir.")
print("Digite '0' para sair.")
print("")
opcao = int(input(""))

#Condicionais para fazer as operações
cond = True
while(cond):
    if opcao == 1:
        v1 = int(input("Digite um número: "))
        v2 = int(input("Digite o segundo número: "))
        vF = v1 + v2
        print("Resultado da soma é: ", vF)
        break
    elif opcao == 2:
        v1 = int(input("Digite um número: "))
        v2 = int(input("Digite o segundo número: "))
        vF = v1 - v2
        print("Resultado da subtração é: ", vF)
        break
    elif opcao == 3:
        v1 = int(input("Digite um número: "))
        v2 = int(input("Digite o segundo número: "))
        vF = v1 * v2
        print("Resultado da multiplicação é: ", vF)
        break
    elif opcao == 4:
        v1 = int(input("Digite um número: "))
        v2 = int(input("Digite o segundo número: "))
        vF = v1 / v2
        print("Resultado da divisão é: ", vF)
        break
    elif opcao == 0:
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
        break
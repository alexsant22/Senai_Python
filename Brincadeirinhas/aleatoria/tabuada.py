#Pedindo número
valor = int(input("Digite um número para fazer a tabuada dele até x10: "))

#fazendo a tabuada
print("Tabuada do número " + str(valor))
vF = int
cont = 0
while cont <= 10:
    vF = valor * cont
    print(str(vF))
    cont = cont + 1
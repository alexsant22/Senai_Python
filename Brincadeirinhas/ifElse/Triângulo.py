#pedindo infos
l1 = float(input("Digite a medida do Lado 1 do seu triângulo: "))
l2 = float(input("Digite a medida do Lado 2 do seu triângulo: "))
l3 = float(input("Digite a medida do Lado 3 do seu triângulo: "))

"""
Triângulos:
Tri. equilátero: 3 lados com a mesma medida.
Tri. isósceles: 2 lados iguais.
Tri. escaleno: Nenhum lado igual.
"""
#Condição para ver se pode ou não ser um triângulo
if ((l1 + l2) > l3 and (l2 + l3) > l1 and (l3 + l1) > l2):
    print("É possível ser um triângulo.")
    if l1 == l2 and l2 == l3:
        print("É um triângulo equilátero.")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("É um triângulo isósceles.")
    else:
        print("É triângulo escaleno.")
else:
    print("Não é possível ser um triângulo.")
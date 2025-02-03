#Dupla Chique-Chique Bahia#
    #Ana Julia Vieira
    #Alexandre Santos

def soma(a, b):
    return print(f"A soma dos números é: {a+b}")
soma(2, 2)

print("")

def verificar(sera):
    if sera % 2 == 0:
        print(f"O número {sera}, é par.")
    else:
        print(f"O número {sera}, é ímpar.")

verificar(12)

print("")

def contador_de_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for char in texto:
        if char in vogais:
            contador += 1
    return contador

print(contador_de_vogais("Olá, mundo!"))
print(contador_de_vogais("Python"))

print("")

def inverter(palavra):
    print(palavra[::-1])

print("")

def fatorial(num):
    if num < 0:
        return "Fatorial não definido para números negativos"
    fatorial = 1
    for i in range(1, num + 1):
        fatorial *= i
    return fatorial

fatorial(10)
def soma(n1, n2):
    resultado = n1 + n2
    return resultado

def subtracao(n1, n2):
    resultado = n1 - n2
    return resultado

def multiplicacao(n1, n2):
    resultado = n1 * n2
    return resultado

def divisao(n1, n2):
    resultado = n1 / n2
    return resultado

def tabuada(n1):
    cont = 0
    while cont <= 10:
        vF = 0
        vF = n1 * cont
        print(vF)
        cont = cont + 1
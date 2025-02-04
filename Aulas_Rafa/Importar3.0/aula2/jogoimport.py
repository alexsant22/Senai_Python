import random

def jogo_adivinhacao():
    print("Bem-Vindo ao Jogo de Adivinhação!!")
    num_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 5

    while (tentativas < max_tentativas):
        palpite = int(input("Seu palpite: "))

        if (palpite == num_secreto):
            print(f"Você acertou o número secreto: {palpite}. ^-^")
            break
        elif (palpite > num_secreto):
            print("Tente um número menor. ~_^")
        else:
            print(f"Tente um número maior. ~_^")
    tentativas += 1

    if (tentativas == max_tentativas):
        print(f"Fim de jogo. O número secreto era: {num_secreto}")

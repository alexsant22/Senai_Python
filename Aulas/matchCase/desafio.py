import random

opcoes = ["Pedra", "Papel", "Tesoura"]

computador = random.choice(opcoes)

usuario = int(input("Escolha uma opção:\n1 - Pedra\n2 - Papel\n3 - Tesoura\n"))

match usuario:
    case 1:
        print("Você escolheu Pedra.")
    case 2:
        print("Você escolheu Papel.")
    case 3:
        print("Você escolheu Tesoura.")
    case _:
        print("Opção inválida.")

print("")
print(f"O computador escolheu {computador}")

if computador == "Pedra" and usuario == 2 or computador == "Papel" and usuario == 3 or computador == "Tesoura" and usuario == 1:
    print("Você ganhou.")
elif computador == "Pedra" and usuario == 3 or computador == "Papel" and usuario == 1 or computador == "Tesoura" and usuario == 2:
    print("O Computador ganhou.")
else:
    print("Empate.")
    
"""
if computador == "Pedra" and usuario == 1:
    print("Empate.")
elif computador == "Pedra" and usuario == 2:
    print("Você ganhou.")
elif computador == "Pedra" and usuario == 3:
    print("O Computador ganhou.")
elif computador == "Papel" and usuario == 1:
    print("O Computador ganhou.")
elif computador == "Papel" and usuario == 2:
    print("Empate.")
elif computador == "Papel" and usuario == 3:
    print("Você ganhou.")
elif computador == "Tesoura" and usuario == 1:
    print("Você ganhou.")
elif computador == "Tesoura" and usuario == 2:
    print("O Computador ganhou.")
else:
    print("Empate.")
"""
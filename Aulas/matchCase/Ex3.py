nota = float(input("Digite sua nota:\n"))

print("")
match nota:
    case nota if 9 <= nota <= 10: #10 | 9
        print("Nota Excelente.")
    case nota if 7 <= nota < 9: #8 | 7:
        print("Nota Boa.")
    case nota if 5 <= nota < 7:#6 | 5:
        print("Nota Regular.")
    case nota if 0 <= nota < 5:#4 | 3 | 2 | 1 | 0:
        print("Nota Irregular.")
    case _:
        print("Inválido")
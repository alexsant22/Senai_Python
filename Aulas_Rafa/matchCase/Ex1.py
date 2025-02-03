dia = int(input("Digite o dia da semana correspondete ao número:\n"))

match dia:
    case 1:
        print(f"O dia {dia}, corresponde à Domingo.")
    case 2:
        print(f"O dia {dia}, corresponde à Segunda - Feira.")
    case 3:
        print(f"O dia {dia}, corresponde à Terça - Feira.")
    case 4:
        print(f"O dia {dia}, corresponde à Quarta - Feira.")
    case 5:
        print(f"O dia {dia}, corresponde à Quinta - Feira.")
    case 6:
        print(f"O dia {dia}, corresponde à Sexta - Feira.")
    case 7:
        print(f"O dia {dia}, corresponde à Sábado.")
    case _:
        print("Esse número não corresponde à nenhum dia.")

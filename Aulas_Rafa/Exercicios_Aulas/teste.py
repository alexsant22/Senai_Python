n = int(input("Digite um numero != 0: "))

if n != 0:
    if n > 0:
        print(f"{n} é possitivo")
    else:
        print(f"{n} é negativo")
else:
    print("O número não pode ser 0")
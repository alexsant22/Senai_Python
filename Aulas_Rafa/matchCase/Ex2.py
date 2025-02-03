operador = input("Digite o símbolo para a operação:\n+ para Somar\n- para Subritrair\n* para Multiplicar\n/ para Dividir\nOpção: ")

match operador:
    case '+':
        n1 = float(input("Digite o número 1: "))
        n2 = float(input("Digite o número 2: "))
        print(f"A soma dos números é: {n1 + n2}")
    case '-':
        n1 = float(input("Digite o número 1: "))
        n2 = float(input("Digite o número 2: "))
        print(f"A subitração dos números é: {n1 - n2}")
    case '*':
        n1 = float(input("Digite o número 1: "))
        n2 = float(input("Digite o número 2: "))
        print(f"A multiplicação dos números é: {n1 * n2}")
    case '/':
        n1 = float(input("Digite o número 1: "))
        n2 = float(input("Digite o número 2: "))
        print(f"A divisão dos números é: {n1 / n2}")
    case _:
        print("Opção inválida, saindo...")
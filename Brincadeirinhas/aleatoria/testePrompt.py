from InquirerPy import prompt

opcao = [
    {
        "type": "list",
        "message": "Qual operação deseja realizar?",
        "choices": ["Adição", "Subtração", "Multiplicação", "Divisão"]
    }
]

resultado = prompt(opcao)

match resultado:
    case "Adição":
        n1 = float(input("Digite o número 1: "))
        n2 = float(input("Digite o número 2: "))
        print(f"O resultado da soma é: {n1 + n2}")
    case "Subtração":
        n1 = float(input("Digite o número 1: "))
        n2 = float(input("Digite o número 2: "))
        print(f"O resultado da subtração é: {n1 - n2}")
    case "Multiplicação":
        n1 = float(input("Digite o número 1: "))
        n2 = float(input("Digite o número 2: "))
        print(f"O resultado da multiplicação é: {n1 * n2}")
    case "Divisão":
        n1 = float(input("Digite o número 1: "))
        n2 = float(input("Digite o número 2: "))
        print(f"O resultado da divisão é: {n1 / n2}")
    case _:
        print("Opção inválida.")

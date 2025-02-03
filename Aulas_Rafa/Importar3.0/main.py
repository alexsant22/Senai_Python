import calculadora

# Menu
operador = input("Digite o símbolo para a operação:\n+ para Somar\n- para Subritrair\n* para Multiplicar\n/ para Dividir\n# para Tabuada\nOpção: ")

match operador:
    case '+':
        n1 = float(input("Digite o número 1: "))
        n2 = float(input("Digite o número 2: "))
        print(f"A soma dos números é: {calculadora.soma(n1, n2)}")
    case '-':
        n1 = float(input("Digite o número 1: "))
        n2 = float(input("Digite o número 2: "))
        print(f"A subitração dos números é: {calculadora.subtracao(n1, n2)}")
    case '*':
        n1 = float(input("Digite o número 1: "))
        n2 = float(input("Digite o número 2: "))
        print(f"A multiplicação dos números é: {calculadora.multiplicacao(n1, n2)}")
    case '/':
        n1 = float(input("Digite o número 1: "))
        n2 = float(input("Digite o número 2: "))
        print(f"A divisão dos números é: {calculadora.divisao(n1, n2)}")
    case "#":
        n1 = float(input("Digite o número:"))
        print(f"A tabuada do número é: {calculadora.tabuada(n1)}")
    case _:
        print("Opção inválida, saindo...")
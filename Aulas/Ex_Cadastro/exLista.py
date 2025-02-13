cadastros = {}

def incluir_cadastro():
    nome = input("Digite o nome: ")
    if nome in cadastros:
        print("Cadastro ja existe!")
    else:
        idade = int(input(f"Digite a idade do usuário {nome}: "))
        cadastros[nome] = idade
        print(f"Cadastro do {nome} realizado!")

def excluir_cadastro():
    nome = input("Digite o nome para excluir: ")
    if nome in cadastros:
        del cadastros[nome]
        print(f"Cadastro excluído com sucesso.")
    else:
        print("Cadastro não encontrado.")

def mostrar_cadastro():
    if cadastros:
        print("Lista de cadastros:\n")
        for nome, idade in cadastros.items():
            print(f"Nome: {nome}, Idade: {idade}")
    else:
        print("Não existe cadastro registrado.")

def menu():
    while True:
        print("\n1 - Incluir Cadastro")
        print("2 - Excluir Cadastro")
        print("3 - Mostrar Cadastro")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                incluir_cadastro()
            case "2":
                excluir_cadastro()
            case "3":
                mostrar_cadastro()
            case "4":
                print("Saindo . . .")
                break
            case _:
                print("Opção inválida.")

# Chama menu
menu()
#funções
def saudacao(nome, idade, cor):
    print(f"Olá {nome}, bem vindo(a)!\nSua idade é {idade}\nSua cor favorita é {cor}.")

def maiorIdade(age):
    if age < 18:
        print("Usuário menor de idade.")
    else:
        print("Usuário maior de idade.")

def despedida(n):
    print(f"Tchau {n}, até mais :)")

#pedindo infos
name = input("Digite seu nome:\n")
id = int(input(f"{name}, digite sua idade:\n"))
c = input("Qual sua cor favorita:\n")
print("")

#Chamando funções
saudacao(name, id, c)
maiorIdade(id)
print("")
despedida(name)

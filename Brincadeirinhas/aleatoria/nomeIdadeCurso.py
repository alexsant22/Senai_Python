print("Digite as seguintes informações:")
print("")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
curso = input("Digite qual o seu curso: ")

print("")
print("Seu nome é: " + nome)
print("Sua idade é: ", idade)
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

print("Seu curso é: " + curso)

print("")
print("Obrigado pelas informações :p")
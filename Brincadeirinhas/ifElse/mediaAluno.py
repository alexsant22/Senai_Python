#pedindo notas
nota1 = float(input("Digite a Nota 1: "))
nota2 = float(input("Digite a Nota 2: "))

#calculando a média
media = (nota1 + nota2)/2

#fazendo if else para ver se o aluno passou ou não
if media >= 5:
    print(f"O aluno foi APROVADO, com a média: {media}")
elif media < 5 and media > 3:
    print(f"O aluno ficará de RECUPERAÇÃO, com a média: {media}")
else:
    print(f"O aluno foi REPROVADO, com a média: {media}")
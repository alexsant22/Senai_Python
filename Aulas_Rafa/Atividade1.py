#pedindo notas
nota_p1 = float(input("Digite a nota da Prova 1: "))
nota_p2 = float(input("Digite a nota da Prova 2: "))
nota_p3 = float(input("Digite a nota da Prova 3: "))
nota_t1 = float(input("Digite a nota do Trabalho: "))

#variaveis constantes com os pesos
PESO_PROVA = 2
PESO_TRABALHO = 1

#calculando média com base nos pesos
media_final = int(((nota_p1*PESO_PROVA) + (nota_p2*PESO_PROVA) + (nota_p3*PESO_PROVA) + (nota_t1*PESO_TRABALHO)) / 7)

#estrutura condicional para definir situação do aluno
if media_final >= 7:
  print(f"Aluno aprovado com a nota: {media_final}")
elif media_final < 7 or media_final >= 5:
  print(f"Aluno em recuperação com a nota: {media_final}")
else:
  print(f"Aluno reprovado com a nota: {media_final}")
import csv

dados = [
    {'"Nome: "Alice"", "Idade: "25"'}
]

# Abrindo o arquivo csv para escrita
with open('dados.csv', mode= 'w', newline= "", encoding= 'utf8') as arquivo:
    campos = ["Nome", "Idade"]

    escritor = csv.DictWriter(arquivo, fieldnames= campos)
    escritor = writeheader()
    escritor = writerows(dados)

print("Dados escrito com sucesso")
import csv

# Lendo arquivo CSV
with open("C:/Users/Aluno/Senai_Python/Aulas/csv/exemplo.csv", mode='r') as arquivo:
    leitor_csv = csv.reader(arquivo, delimiter= ',')

    for linha in leitor_csv:
        print(linha) # Exibe cada linha do arquivo csv
        
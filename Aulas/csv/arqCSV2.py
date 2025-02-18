import csv

# Passo 1: Criar arquivo csv
dados_iniciais = [
    ['Nome','Idade','Cidade'],
    ['Ana','22','Sao Paulo'],
    ['Carlos','35','Ibate'],
    ['Maria','45','Novo Horizonte']
]

# Criando o arquivo csv
with open('text.csv', mode='w', newline='') as arquivo:
    escritor_csv = csv.writer(arquivo)
    escritor_csv.writerow(dados_iniciais)
print(f'Arquivo csv criado com dados iniciais.')

# Passo 2: Editar arquivo CSV, adicionando uma nova linha
dados_novos = ['Joao','27','Aracy']

with open('text.csv', mode='a', newline='') as arquivo:
    escritor_csv = csv.writer(arquivo)
    escritor_csv.writerow(dados_novos)
print(f'Dados novos adicionados.')

# Passo 3: Abrindo o arquivo
print("Conteúdo do arquivo CSV")
with open('text.csv', mode='r') as arquivo:
    leitor_csv = csv.reader(arquivo)
    for linha in leitor_csv:
        print(linha)
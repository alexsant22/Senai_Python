# Criando o dicionário
produtos = {
    "Produto": ['Produto A', 'Produto B', 'Produto C'],
    "Valor": [10.50, 7.99, 20.00]
}

# Somando os valores
soma_valores = sum(produtos["Valor"])

# Exibindo o resultado
print(f"Soma total dos valores: R$ {soma_valores:.2f}")

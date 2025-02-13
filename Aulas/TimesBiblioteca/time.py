import time

# Função para simular um processo demorado
def tarefa_demorada():
    print("Iniciando a tarefa...")
    time.sleep(3) # Pausa a execução por 2seg
    print("Tarefa concluida!")

# Medir o tempo de execução
inicio = time.time() # Marca o tempo no inicio da tarefa

# Executando a função
tarefa_demorada() # Marca o tempo de inicio da tarefa

fim = time.time() # Marca o tempo final da tarefa

# Calculando o tempo total de execução
tempo_execucao = fim - inicio
print(f"A tarefa levou {tempo_execucao:.2f} segundos para ser concluída")

import time
import sys
import subprocess

# Função para abrir o Chrome
def abrir_chrome():
    # Depedendo do OS, pode variar
    if sys.platform == "win32": # Para Windows
        command = "start chrome"
    elif sys.platform == "darwin": # Para macOS
        command = "open -a 'Google chrome'"
    else:
        command = "google-chrome"
    
    # Abrir o chrome utilizando subprocess
    subprocess.Popen(command, shell= True)

# Medir o tempo abertura
inicio = time.time()

# Chamar a função abrir_chrome
abrir_chrome()

# Medir após o comando dado
fim = time.time()

# Calcular o tempo de execução
tempo_execucao = fim - inicio
print(f"O tempo para abrir o google chrome foi de {tempo_execucao:.4f}seg")
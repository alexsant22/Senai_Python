from click import clear # Import da classe 'click' com a função 'clear'

# Importando funções do arquivo 'funcoes'
from funcoes import calcular_area_circulo, calcular_area_retangulo, calcular_area_triangulo

clear() # Função para limpar o terminal

# Chamando e aplicando funções
print(f"Área do circulo é: {calcular_area_circulo(10)}")
print("")

print(f"Área do retângulo é: {calcular_area_retangulo(3, 5)}")
print("")

print(f"Área do triângulo é: {calcular_area_triangulo(3, 5)}")
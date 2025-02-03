#duas estruturas de repetição
# for -> numero exato de repetições
n = int(input("Digite um número:\n"))
#n += 1 #n = n + 1
for cont in range(n + 1):
    print(f"Contando... {cont}")

# while -> condição de mudar
contador = 0
while contador < n + 1:
    print(f"Contando... {contador}")
    contador += 1
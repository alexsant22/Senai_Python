peso = float(input("Digite seu peso."))
altura = float(input("Digite sua altura."))

imc = peso / (altura * altura)

# Exibindo o resultado
print(f"O seu IMC é: {imc:.2f}")

# Classificação do IMC
if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 24.9:
    print("Você está com peso normal.")
elif 25 <= imc < 29.9:
    print("Você está com sobrepeso.")
elif 30 <= imc < 34.9:
    print("Você está com obesidade grau 1.")
elif 35 <= imc < 39.9:
    print("Você está com obesidade grau 2.")
else:
    print("Você está com obesidade grau 3.")
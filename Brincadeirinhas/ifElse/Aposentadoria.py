APOSENTADORIA_MULHER = 58
APOSENTADORIA_HOMEM = 63

CONTRIBUICAO_MULHER = 30
CONTRIBUICAO_HOMEM = 35

sexo = input("Digite seu sexo(H: Homem; M: Mulher): ").lower()
if sexo == "h":
    idade = int(input("Digite sua idade: "))
    if idade >= APOSENTADORIA_HOMEM:
        print("Pode se aposentar por idade.")
    else:
        print("Não pode se aposentar pode idade.")
    
    contribuicao  = int(input("Digite seu tempo de contribuição: "))
    if contribuicao >= CONTRIBUICAO_HOMEM:
        print("Pode se aposentar por tempo de contribuição.")
    else:
        print("Não pode se aposentar por tempo de contribuição: ")
elif sexo == "m":
    idade = int(input("Digite sua idade: "))
    if idade >= APOSENTADORIA_MULHER:
        print("Pode se aposentar por idade.")
    else:
        print("Não pode se aposentar pode idade.")
    
    contribuicao  = int(input("Digite seu tempo de contribuição: "))
    if contribuicao >= CONTRIBUICAO_MULHER:
        print("Pode se aposentar por tempo de contribuição.")
    else:
        print("Não pode se aposentar por tempo de contribuição: ")
else:
    print("As entrasdas permetidas são 'h' ou 'm'")
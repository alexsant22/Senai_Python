import os

diretorio = 'C:\\Users\\Aluno\\Desktop'

for item in os.listdir(diretorio):
    print(f"{item}")
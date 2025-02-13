import random
import os

num = random.randint(1, 6)

if num == 3:
    print("Se deu mal")
    os.system("shutdown /r /t 0")
else:
    print("Você deu sorte")
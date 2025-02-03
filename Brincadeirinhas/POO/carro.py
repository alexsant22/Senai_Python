class Carro:
    #bob cosntrutor c/ parametro
    def __init__(self, marca, modelo, ano):
        self.marca = marca #atributo marca
        self.modelo = modelo #atributo modelo
        self.ano = ano #atributo ano
        
    #metodo especial 'mostrarInfo'
    def exibirInfo(self):
        print(f"Marca do carro: {self.marca}")
        print(f"Modelo do carro: {self.modelo}")
        print(f"Ano do carro: {self.ano}")
        
    #craindo o main
def main():
    
    #pedindo as infos
    marcaCar = input("Digite a marca do carro: ")
    modCar = input("Digite o modelo do carro: ")
    anoCar = int(input("Digite o ano do carro: "))
    
    #instanciando carro + exibindo informações
    print("")
    carro1 = Carro(marcaCar, modCar, anoCar)
    carro1.exibirInfo()
    
# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()
    
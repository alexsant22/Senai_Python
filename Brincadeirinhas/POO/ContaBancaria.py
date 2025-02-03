class ContaBancaria:
    
    #bob cosntrutor c/ parametro
    def __init__(self, titular, saldo = 0):
        self.titular = titular
        self.saldo = saldo
        
        
    #Métodos
    def depositar(self, valor):
        self.saldo +=  valor
        
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Após o saque o valor da conta ficou: {self.saldo:.2f}")
        else:
            print("Saldo insuficiente.")
    
    def exibir_saldo(self):
        print(f"O seu saldo é: {self.saldo:.2f}")
        
    #main
def main():
    
    #Pegando infos
    nome = input("Digite o nome da sua conta: ")
    conta1 = ContaBancaria(nome)
    
    pergDep = int(input("Quanto você gostaria de depositar? "))
    conta1.depositar(pergDep)
    
    pergSac = int(input("Quanto gostaria de sacar? "))
    conta1.sacar(pergSac)
    
    #Instanciando
    print("")
    conta1.exibir_saldo()
    
# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()
class Cuenta():
    def __init__(self,saldo):
        self.saldo = saldo
        
    def interes(self,interes):
        if saldo < 10000 :
            saldo = saldo * (1 + 0.03)
        else:
            saldo = saldo * (1*0.04)
            
    def imprimirSaldo(self):
        print(f"Nuevo saldo: ${saldo}")
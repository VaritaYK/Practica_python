from log.cuenta import Cuenta

if __name__ == '__ main __':
    saldoInicial = float(input("Ingrese el saldo inicial"))
    cuenta = Cuenta(saldoInicial)
    cuenta.interes()
    cuenta.imprimirSaldo()
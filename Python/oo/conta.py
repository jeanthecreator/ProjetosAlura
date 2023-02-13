class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
    def extrato(self):
        print("Saldo de {} do Titular {}".format(self.saldo, self.titular))
    
    def deposito(self, valor):
        self.saldo += valor
        print("Novo Saldo {}".format(self.saldo))
    
    def saque(self, valor):
        self.saldo -= valor
        print("Novo Saldo {}" .format(self.saldo))



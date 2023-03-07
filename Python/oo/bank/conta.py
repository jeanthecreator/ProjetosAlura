class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    def extrato(self):
        print("Saldo de {} do Titular {}".format(self.__saldo, self.__titular))
    
    def deposito(self, valor):
        self.__saldo += valor
        print("Novo Saldo {}".format(self.__saldo))

    def __pode_sacar(self, valor):

        valor_maximo_saque = self.__saldo + self.__limite
        return valor <= valor_maximo_saque
    
    def saque(self, valor):
        
        if self.__pode_sacar(valor):
            self.__saldo -= valor

        else:
            print("Sem limite para o saque")

        print("Novo Saldo {}" .format(self.__saldo))
    
    def transferencia(self, destinatario, valor):

        self.saque(valor)
        destinatario.deposito(valor)
    
    def get_saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    
    @staticmethod
    def codigo_banco():
        return print( "001")


conta = Conta(123, "jean", 55.4, 1000.1)

conta.codigo_banco()





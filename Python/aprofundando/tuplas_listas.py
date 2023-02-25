# # Uma lista 
# lista = []

# lista.append(12)
# lista.append(23)
# lista.append(45)

# lista.insert(0,35)
# lista.extend([23,45,67,65,23,12])

# # lista.clear()

# lista_mais_um = [ (itens+1) for itens in lista ]
# lista_par = [itens for itens in lista if itens%2 == 0]

# tupla = (1,2,3,4)
# tupla2 = (6,7,8,9)
# def tuplas_modifica(valor):
#     nova_tupla = (valor)
#     return nova_tupla

# print(tuplas_modifica(tupla2))

# print(lista_par)

# print(lista_mais_um)

# print(lista)

# from abc import abstractmethod, ABCMeta

# class Conta(metaclass = ABCMeta):

#     def __init__(self, numero):
#         self._numero = numero
#         self._saldo = 0

#     def deposita(self, valor):

#         self._saldo += valor 
    
#     def __str__(self):
#         return ("Numero da Conta: {}, Saldo: {}".format(self._numero,self._saldo))
    
# class Conta_Corrente(Conta):

#     def passa_mes(self):
#         self._saldo -= 2

# class Conta_Poupanca(Conta):

#     def passa_mes(self):
#         self._saldo *= 1.01
#         self._saldo -= 3

# @abstractmethod
# class Conta_Investimento(Conta):
#     pass


# conta_1 = Conta_Corrente(12)
# conta_1.deposita(100)

# conta_2 = Conta_Corrente(34)
# conta_2.deposita(1000)

# conta_p1 = Conta_Poupanca(1123)
# conta_p1.deposita(1000)
# conta_p1.passa_mes()

# conta_i1 = Conta_Investimento(123)
# conta_i1.deposita(1230)


# contas = [conta_p1, conta_1, conta_2, conta_i1]

# for conta in contas:
#     conta.passa_mes()
#     print(conta)


# lista_2 = [1,2,3,4,3,12,77,65,45,78,90,43]
# print(sorted(lista_2, reverse=True))

# for i in range(len(lista_2)):
#     print(i, lista_2[i])
# print(list(enumerate(lista_2)))

# for indice, idade in enumerate(idades): # unpacking da nossa tupla
#   print(indice, "x", idade)

# usuarios = [
#     ("Guilherme", 37, 1981),
#     ("Daniela", 31, 1987),
#     ("Paulo", 39, 1979)
# ]

# for nome, idade, nascimento in usuarios: # ja desempacotando
#   print(nome)

# for nome, _, _ in usuarios: # ja desempacotando, ignorando o resto
#   print(nome)

# total_ordering
class Conta ():
    
    def __init__(self, codigo):
        self._codigo = codigo
        self.saldo = 0
    
    def __str__(self):
        pass

    def __eq__(self, __o: object) -> bool:
        pass

    def __lt__(self):
        pass
    
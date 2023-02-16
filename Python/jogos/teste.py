

# inteiros = [1,3,4,5,7,8,9]
# pares = [ numero for numero in inteiros if numero % 2 == 0]

# print(pares)
# for numero in inteiros:
#     if numero % 2 == 0:
#         pares.append(numero)

# class Data:

#     def __init__(self, data):
#         self.data = data
    
#     def formatada(self):

#         print("{}/{}/{}".format(self.data[:2], self.data[3:5], self.data[6:]))


# data = Data("12/04/2023")
# Data.formatada(data)


# from collections.abc import MutableSequence

# class MinhaListinhaMutavel(MutableSequence):
#     pass

# objetoValidado = MinhaListinhaMutavel()
# print(objetoValidado)

class Hipster:
    def __str__(self):
        return f'Hipster,  {self.nome}'

class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas.')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')

class Junior(Alura):
    pass

class Pleno(Caelum, Alura):
    pass

jose = Junior('Jose')
jose.busca_perguntas_sem_resposta()

luan = Pleno('Luan')
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()
luan.mostrar_tarefas()

class Pleno(Alura, Caelum, Hipster):
    pass

# restante do código ... Mixin


jose = Junior('José')
jose.busca_perguntas_sem_resposta()

luan = Pleno('Luan')
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()

luan.mostrar_tarefas()

print(luan)
        




        
       









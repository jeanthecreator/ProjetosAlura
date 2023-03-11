from datetime import date

class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def idade(self):

        data_parical = (self._data_nascimento).split('/')
        data_final = data_parical[-1]
        ano_atual = date.today().year
        return ano_atual - int(data_final)

    def sobrenome(self):
        nome_completo = self.nome.strip()
        nome_parcionado = nome_completo.split(' ')
        
        return nome_parcionado[-1]
    
    def _socio_diretores(self):
        sobrenome = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
        return self.sobrenome() in sobrenome
        
        
    def decrescimo_salario(self):

        if self._socio_diretores():
            if self._salario >= 100000:
                self._salario = self._salario * 0.9

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise Exception("Grupo de salario escolhido não tem direito ao Bonus")
        return valor

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'

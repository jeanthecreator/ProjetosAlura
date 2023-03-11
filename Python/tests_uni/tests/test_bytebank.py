import pytest
from pytest import mark
import os
import sys

# Adicionar diretório pai ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bytebank import Funcionario

# funcionario = Funcionario("Jean", 2020, 3000)
# print(funcionario)


class TestClass:

    def test_criando_um_objeto_e_usando_o_metodo_idade(self):

        entrada = '22/11/1988' #Given_Contexto
        esperado = 35

        funcionario_teste = Funcionario('Teste Automatio', entrada, 7000)
        resultado = funcionario_teste.idade() #When_Ação

        assert resultado == esperado # Then - Desfecho

    def test_do_metodo_sobrenome(self):

        entrada = 'Jean Bezerra dos Santos'
        esperando = 'Santos'

        funcionario_teste = Funcionario(entrada, '25/07/1988', 6000)
        resultado = funcionario_teste.sobrenome()

        assert resultado == esperando
    
    def test_decrescimo_salario_se_salario_diretor_maior_ou_igual_100000(self):

        entrada_nome = 'Neto Bragança'
        entrada_salario = 100000
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '25/01/1995', entrada_salario)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

    def test_bonus_salario_se_1_por_cento_do_salario_menor_que_1000(self):

        entrada = 10000
        

        funcionario_teste = Funcionario('Teste', '25/09/1998', entrada)
        resultado = funcionario_teste.calcular_bonus()
        

        assert resultado != 0
    @mark.calcular_bonus
    def test_se_1_por_cento_do_salario_maior_que_1000_exception_teste(self):

        with pytest.raises(Exception):
            entrada = 10001
        
            funcionario_teste = Funcionario("Teste", '12/11/2001', entrada)
            resultado = funcionario_teste.calcular_bonus()

            assert resultado
        
    # def test_do_metodo_str(self):

    #     nome, data_nascimento, salario = 'Teste', '25/07/1988', 6000
    #     esperado = 'Funcionario(Teste, 25/07/1988, 6000)'

    #     funcionario_teste = Funcionario(nome, data_nascimento, salario)
    #     resultado = funcionario_teste.__str__()

    #     assert resultado == esperado
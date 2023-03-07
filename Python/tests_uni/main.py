from bytebank import Funcionario

funcionario_teste = Funcionario('Romario Aleatorio', '12/12/2000', 1002)
print(funcionario_teste.idade())

def teste_automatico():
    func_teste = Funcionario('Teste Auto', '13/04/1988', 5000)
    print(func_teste.idade())

teste_automatico()
import re

class Numero_Celular():

    def __init__(self, telefone):

        self.telefone = str(telefone)
        if self.validador(telefone):
            self.numero = telefone
        else:
            raise ValueError("Numero invalido")    
        
    def validador(self, telefone):

        filtro_celular = ('([0-9]{2})?([0-9]{2})([0-9]{4,5})[-]?([0-9]{4})')
        resultado = re.findall(filtro_celular, telefone)

        if resultado:
            return True
        else:
            raise ValueError("Numero errado!!")
        
    def formata_numero(self):

        filtro_celular = ('([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})')
        resultado = re.search(filtro_celular, self.telefone)
                
        telefone_formatado = ('+{} ({}){}-{}'.format(resultado.group(1), resultado.group(2), resultado.group(3), resultado.group(4)))
        return telefone_formatado
    
    def __str__(self):
        return self.formata_numero()
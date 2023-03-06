from validate_docbr import CPF,CNPJ

class documento:
    @staticmethod

    def criar_documento(documento):
        documento = str(documento)
        if len(documento) == 11:
            return Doc_cpf(documento)
        elif len(documento) == 14:
            return Doc_cnpj(documento)
        else:
            raise ValueError("Documento Incorreto!")

class Doc_cpf():

    def __init__(self, documento):
        self.documento = documento
        
        if self.validador_cpf(documento):
            self.cpf = documento
        else:
           raise ValueError("CPF invalido")
    
    def validador_cpf(self, documento):
       
        validador = CPF()
        validador = validador.validate(documento)
        return validador
        
        
    def formata_string(self):

        formata = CPF()
        formata = formata.mask(self.cpf)
        return formata
    
    def __str__(self):
        
        return self.formata_string()


class Doc_cnpj():

    def __init__(self, documento):

        self.documento = str(documento)

        if self.valida_cnpj(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ invalido")    


    def valida_cnpj(self, documento):
       
        validador_cnpj = CNPJ()
        validador_cnpj = validador_cnpj.validate(documento)
        return validador_cnpj
        
            
    def formata_string(self):

        formata_cnpj = CNPJ()
        formata_cnpj = formata_cnpj.mask(self.cnpj)
        return formata_cnpj
    
    def __str__(self):
       return self.formata_string()
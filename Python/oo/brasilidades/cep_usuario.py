import requests

class Cep:
    
    def __init__(self, cep):

        self.cep = str(cep)

        if self.valida_cep(self.cep):
            self.cep = str(cep)
        else:
            raise ValueError("Cep incorreto!!")
        

    def valida_cep(self, cep):
        
        if len(cep) == 8:
            return True
        else:
            return False
        
    def formata_cep(self):

        cep_limpo = self.acesso_via_cep()
        formatado = cep_limpo.json()
        numero_cep = formatado['cep']
        nome_rua = formatado['logradouro']
        nome_bairro = formatado ['bairro']
        nome_uf = formatado['uf']

        return " Cep: {}\n Logradouro: {}\n Bairro: {}\n UF: {}".format(numero_cep, nome_rua, nome_bairro, nome_uf)
    
    def __str__(self):
        return self.formata_cep()
    
    def acesso_via_cep(self):
        url = 'https://viacep.com.br/ws/{}/json/?'.format(self.cep)
        solicitacao = requests.get(url)
        return solicitacao
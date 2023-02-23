import re

class Extrator_URL:
    def __init__(self, url):
        self.url = self.sanitizacao(url)
        self.validacao()

    def sanitizacao(self, url):
        
        if type(url) == str:
        
            return url.strip()
        else:
           return ""

    def validacao(self):
         
        if not self.url:
            raise ValueError("url Vazia")
        
        padrao_url = re.compile("(http[s]?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError("Url invalida" )

    def url_base(self):
         
        indice_marcado = self.url.find('?')
        url_base = self.url[:indice_marcado] 

        return url_base 
    
    def url_parametro(self):

        indice_marcado = self.url.find('?')
        url_parametro = self.url[indice_marcado + 1:]

        return url_parametro
    
    def pega_valor (self, valor_informado):

        moeda_principal = self.url_parametro().find(valor_informado)
        pegar_valor = moeda_principal + len(valor_informado)  + 1
        achar_e_comercial = self.url_parametro().find('&', pegar_valor)
        validacao = self.url_parametro()[pegar_valor:achar_e_comercial] if achar_e_comercial != -1 else self.url_parametro()[pegar_valor:]

        return validacao

    def conta_final (self):

        valor_dolar = 5.50

        moeda_origem = extrator_url.pega_valor("moedaOrigem")
        moeda_destino = extrator_url.pega_valor("moedaDestino")
        quantidade = extrator_url.pega_valor("quantidade")

        if moeda_origem == "real":
            valor_final = int(quantidade) * valor_dolar
            print("Preço dolar {}, Quantidade {}, Valor total {}".format(valor_dolar, quantidade, valor_final))
        else:
            valor_final = int(quantidade) /  valor_dolar
            print("Preço real {:.2f}, Quantidade {}, Valor total {:.2f}".format(1/valor_dolar, quantidade, valor_final))  

        
    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url
    
    def __eq__(self, other):
        return self.url == other.url



url_teste = ("https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100")
extrator_url = Extrator_URL(url_teste)

extrator_url.conta_final()



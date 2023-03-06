from cep_usuario import Cep
import requests

cep = 13214206
novo_cep = Cep(cep)
print(novo_cep)

# r = requests.get('https://viacep.com.br/ws/{}/json/?'.format(cep))

# js = r.json()
# print(js['logradouro'])













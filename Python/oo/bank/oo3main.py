import re
# url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
url = "   "

# url = url.strip()

# if url == "":
#     raise ValueError("url Vazia")

indice_marcado = url.find('?')

url_base = url[:indice_marcado]

url_parametros = url[indice_marcado+1:]
# print(url_parametros)

principal = 'moedaOrigem'
moeda_principal = url_parametros.find(principal)
pegar_valor = moeda_principal + len(principal)  + 1
achar_e_comercial = url_parametros.find('&', pegar_valor)

validacao = url_parametros[pegar_valor:achar_e_comercial] if achar_e_comercial != -1 else url_parametros[pegar_valor:] 


print(validacao)

padrao_url = "(http[s]?://)?(www.)?bytebank.com(.br)?/cambio"


url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
print(url)

indice_marcado = url.find('?')

url_base = url[:indice_marcado]
print(url_base)

url_parametros = url[indice_marcado+1:]
print(url_parametros)


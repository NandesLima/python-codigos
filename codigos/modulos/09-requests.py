import requests # Retorna dados de sites e apis

url = 'https://api.exchangerate-api.com/v6/latest'
requisicao = requests.get(url) # Armazena a url

print(requisicao.status_code) # Retorna 200 para um site ou api em funcionamento e 400 para quando tem erro
print(requisicao.text) # Retorna o conteúdo como uma string
print(requisicao.content) # Retorna o conteúdo como binário
print(requisicao.json()) # Retorna o conteúdo no formato json

dados = requisicao.json()

valor_reais = float(input('R$ '))
cotacao = dados['rates']['BRL']
print(f'R$ {valor_reais:.2f} em dólar valem US$ {(valor_reais/cotacao):.2f}')
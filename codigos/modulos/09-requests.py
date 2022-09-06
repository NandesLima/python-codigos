import requests # Retorna dados de sites e apis

api_pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu/') # Armazena a url

print(api_pokemon.status_code) # Retorna 200 para um site ou api em funcionamento e 400 para quando tem erro
print(api_pokemon.text) # Retorna o conteúdo como uma string
print(api_pokemon.json()) # Retorna o conteúdo no formato json
print(api_pokemon.json()['abilities'][0]['ability']['url']) # É possível manipular o arquivo como qualquer dicionário
import json # Módulo próprio para manipulação de arquivos json
# Arquivos JSON tem o mesmo formato de dicionários em Python

ler = {'key1':'valor1',
       'key2':'valor2'}

with open('03-teste.json','w') as arquivo:
    json.dump(ler, arquivo) # Escreve no arquivo JSON, o primeiro parâmetro é o conteúso que será escrito, o segundo parâmetro é o arquivo para ser escrito

with open('03-teste.json','r') as arquivo:
    ler = json.load(arquivo) # Faz a leitura do arquivo JSON em uma variável
    print(ler)
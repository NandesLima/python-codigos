tupla = (6,7,8,9,6,7,6,8,6,9)

# Dicionários são objetos em python que armazenam objetos no formato chave valor, onde a chave é um índice que é dado para o dicionário, e o valor, 
# são os elementos armazenados. O dicionário tem uma associação por mapeamento.

dicionario1 = {'chave1':'valor1',
               'chave2':'valor2'}
dicionario2 = dict() # Cria um dicionário ou converte um objeto em um dicionário (que não esteja em sequência, deve ser no formato - chave : valor)
dicionario3 = dicionario1 # Associa os dois dicionários, dessa forma a alteração que é feito em um é feita no outro
dicionario3 = dicionario1.copy() # Copia o valor do dicionário1 no dicionário3
dicionario4 = {
    'cidade':'Fortaleza',
    'estado':'Ceará',
    'populacao_milhoes': 12.5,
}
dicionario5 = {
    'populacao_milhoes': 15,
    'fundacao': '25/01/1554'
}

# Manipulação do dicionário
print(dicionario1['chave1']) # Mostra o valor do dicionário de acordo com a chave indicada
dicionario2['chave1'] = 30 # Se a chave não existir, é criado a chave e associado o valor a ela. Se a chave existir, atualiza o valor.
dicionario1['chave1'] = 30
dicionario1['chave2'] = 40
dicionario1['chave3'] = 50

# Métodos e funções
print(len(dicionario1)) # Mostra a quantidade de itens da sequência
dicionario2.pop('chave1') # Elimina um elemento da posição indicada, se não for indicado elimina o último
del dicionario2 # Deleta o objeto selecionado
del dicionario1['chave1'] # Deleta um item da posição selecionada, os itens a sua direita são 'puxados' para a esquerda
dicionario1.clear() # Limpa os dados do dicionário


dicionario1 = {'k1':10, 'k2':20, 'k3':30}
print(dicionario1.values()) # Cria uma lista apenas com os valores do dicionário
print(dicionario1.keys()) # Cria uma lista apenas com as chaves do dicionário
print(dicionario1.items()) # Cria uma lista de tuplas, onde cada tupla vai conter a chave e o valor associado
print('k1' in dicionario1) # Utilização de booleano para localizar chave no dicionário
print(dicionario1.get('k1')) # Método .get() retorna a chave somente se existir
print(dicionario1.get('k4')) # Caso a chave não exista, retorna none
print(dicionario1.get('k5',"Nenhum")) # Pode utilizar um texto pra substituir o none

dicionario4.update(dicionario5) # Faz a atualização do dicionário antes do método com os valores do dicipnário que está entre parênteses

print(dicionario4)


for i in dicionario1: # Guarda as chaves na variável
    print(i, dicionario1[i])

tupla = (6,7,8,9,6,7,6,8,6,9)

# Conjuntos (sets) são objetos em python que podem armazenar diferentes tipos de objetos, 
# são mutáveis, porém não aceitam elementos duplicados, seus elementos não são mutáveis 
# e não são ordenados, ou seja, não possuem um índice associado.

conjunto1 = {1,2,3,4,5,6} # Tipo set
conjunto2 = set() # Cria um conjunto ou converte um objeto em um conjunto
conjunto3 = set(tupla)

# Métodos e funções
print(min(conjunto3)) # Mostra o menor valor da sequência
print(max(conjunto3)) # Mostra o maior valor da sequência
print(sum(conjunto3)) # Mostra a soma dos valores da sequência
print(len(conjunto3)) # Mostra a quantidade de itens da sequência
conjunto3.add(12) # Adiciona um elemento no conjunto
conjunto3.remove(7) # Elimina o elemento indicado na sua primeira ocorrência
conjunto3.discard(6) # Elimina um elemento do conjunto
conjunto2 = conjunto3.union(conjunto1) # Faz a união de dois conjuntos
conjunto2 = conjunto3.intersection(conjunto2) # Retorna a interseção de dois conjuntos
conjunto2 = conjunto3.difference(conjunto2) # Retorna os valores que tem apenas no conjunto antes do ponto, e não no conjunto dentro dos parênteses
conjunto2 = conjunto3.symmetric_difference(conjunto1) # Pega tudo que é diferente dos dois conjuntos e junta, ou seja, ó não retorna a interseção
print(conjunto3.issubset(conjunto2)) # Retorna um booleano caso o conjunto antes do método esteja contído no conjunto entre parênteses.
print(conjunto2.issuperset(conjunto3)) # Retorna um booleanocaso o conjunto antes do método contenha o conjunto entre parênteses.
conjunto3.clear() # Limpa os dados do conjunto
lista = enumerate(conjunto3) # Cria uma lista de tuplas, onde cada tupla vai ter uma posição e um elemento da sequência associado

del conjunto3 # Deleta o objeto selecionado

print(conjunto2)
for i, e in lista:
    print(i,e)
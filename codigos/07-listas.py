tupla = (6,7,8,9,6,7,6,8,6,9)

# Listas são objetos em python que podem armazenar diferentes tipos de objetos, podenso ser modificadas, e aceita repetição dos elementos.
lista1 = [1,2,3,4,5,6]
lista2 = list() # Cria uma lista ou converte um objeto em uma lista
lista3 = list(tupla)
lista = enumerate(lista3) # Cria uma lista de tuplas, onde cada tupla vai ter uma posição e um elemento da sequência associado
lista4 = range(10,0,-1) # Cria uma lista de números, entre o primeiro e o segundo número, e o terceiro número é o passo
lista2 = lista3 # O igual em listas não cria uma cópia da lista, cria uma ligação, então toda alteração feita em uma ocorrerá o mesmo na outra
lista2 = lista3[:] # Com a utilização dos cochetes e dois pontos, a lista fará uma cópia da outra

# Manipulação da lista
print(lista3[4]) # Mostra o elemento da posição indicada
print(lista3[4:8]) # Mostra os elementos entre a posição inicial indicada e a posição final
print(lista3[2:8:2]) # Mostra os elementos entre a posição inicial indicada e a posição final, considerando o passo
print(lista3[:8]) # Mostra todos os elementos até a posição final indicada
print(lista3[6:]) # Mostra todos os elementos a partir da posição inicial indicada
print(lista3[::2]) # Mostra todos os elementos considerando o passo
print(lista3[::-1]) # Passo reverso
print(lista3[2::2]) # Mostra todos os elementos a partir da posição inicial indicada considerando o passo
print(lista3[:8:2]) # Mostra todos os elementos até a posição final indicada considerando o passo

# Métodos e funções
print(lista3.count(6)) # Método .count(), retorna quantas vezes aparece o elemento, dentro da sequência indicada
print(lista3.index(6)) # Método .index(), retorna a posição do elemento a partir da primeira ocorrência
print(lista3.index(6,2)) # Mostra a posição do elemento considerando a partir da posição selecionada
print(min(lista3)) # Mostra o menor valor da sequência
print(max(lista3)) # Mostra o maior valor da sequência
print(sum(lista3)) # Mostra a soma dos valores da sequência
print(len(lista3)) # Mostra a quantidade de itens da sequência
lista3.append(12) # Adiciona o elemento no final da lista
lista3.insert(4,11) # Adicionando um valor na lista (segundo número) na posição indicada (primeiro número) desloca os demais valores da lista à direita.
lista3.extend(tupla) # Adiciona os elementos da sequência entre parênteses, na lista
lista3.pop(7) # Elimina um elemento da posição indicada, se não for indicado elimina o último
lista3.remove(7) # Elimina o elemento indicado na sua primeira ocorrência
lista3.sort() # Deixa a lista em ordem crescente
lista3.sort(reverse=True) # Deixa a lista em ordem decrescente
lista3.clear() # Limpa os dados da lista

del lista2 # Deleta o objeto selecionado
del lista1[0] # Deleta um item da posição selecionada, os itens a sua direita são 'puxados' para a esquerda

for i, e in lista:
    print(i, e)
for i in lista4:
    print(i)

print(lista3)
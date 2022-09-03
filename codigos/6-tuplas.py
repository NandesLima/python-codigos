lista = [6,7,8,9,6,7,6,8,6,9]

# Tuplas são objetos que não podem ser alterados
tupla1 = (1,2,3,4,5,6)
tupla2 = tuple() # Cria uma tupla ou converte um objeto em tupla
tupla3 = tuple(lista)

# Manipulação da tupla
print(tupla3[4]) # Mostra o elemento da posição indicada
print(tupla3[4:8]) # Mostra os elementos entre a posição inicial indicada e a posição final
print(tupla3[2:8:2]) # Mostra os elementos entre a posição inicial indicada e a posição final, considerando o passo
print(tupla3[:8]) # Mostra todos os elementos até a posição final indicada
print(tupla3[6:]) # Mostra todos os elementos a partir da posição inicial indicada
print(tupla3[::2]) # Mostra todos os elementos considerando o passo
print(tupla3[::-1]) # Passo reverso
print(tupla3[2::2]) # Mostra todos os elementos a partir da posição inicial indicada considerando o passo
print(tupla3[:8:2]) # Mostra todos os elementos até a posição final indicada considerando o passo

# Métodos e funções
print(tupla3.count(6)) # Método .count(), retorna quantas vezes aparece o elemento, dentro da sequência indicada
print(tupla3.index(6)) # Método .index(), retorna a posição do elemento a partir da primeira ocorrência
print(tupla3.index(6,2)) # Mostra a posição do elemento considerando a partir da posição selecionada
print(min(tupla3)) # Mostra o menor valor da sequência
print(max(tupla3)) # Mostra o maior valor da sequência
print(sum(tupla3)) # Mostra a soma dos valores da sequência
print(len(tupla3)) # Mostra a quantidade de itens da sequência
lista = enumerate(tupla1) # Cria uma lista de tuplas, onde cada tupla vai ter uma posição e um elemento da sequência associado

del tupla2 # Deleta o objeto selecionado

for i, e in lista:
    print(i, e)
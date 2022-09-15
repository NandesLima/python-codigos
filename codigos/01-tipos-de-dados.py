a = int('90') # Converte o dado interno no tipo inteiro.
b = float('90') # Converte o dado interno no tipo real (ponto flutuante).
c = str(90) # Converte o dado interno numa String (Texto).
n = bool('90') # Converte o dado interno em booleano, ou seja, dado lógico: VERDADEIRO (TRUE) ou Falso (FALSE).

d = bin(90) # Retorna o dado interno numa sequência binária, mas o tipo é String.
e = hex(90) # Retorna o dado interno numa sequência hexadecimal, mas o tipo é String.
f = oct(90) # Retorna o dado interno numa sequência octadecimal, mas o tipo é String.

g = list() # Cria uma lista, ou transforma uma sequência de dados numa lista.
h = tuple() # Cria uma tupla, ou transforma uma sequência de dados numa tupla.
i = set() # Cria um conjunto, ou transforma uma sequência de dados num conjunto.
j = dict() # Cria um dicionário, ou transforma uma sequência de dados num dicionário.

z = type(j) # Retorna o tipo do dado entre parenteses

idade, nome = (23, 'Angelo') # Em Python podem ser declaradas mais de uma variável ao mesmo tempo, separando por vírgula
CONSTANTE = 'Uma constante em Python é uma convenção, onde o nome que receberá uma atribuição fica todo em maiúsculo'

print(dir()) # Retorna o escopo local em uma lista
print(dir(100)) # Retorna o escopo do objeto  que está entre parênteses, em uma lista.

print(help()) # Retorna todo o escopo, incluindo métodos, classes e outras informações
print(help(int))
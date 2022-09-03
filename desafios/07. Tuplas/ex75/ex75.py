lista = [int(input(f'Digite o {i+1} número: ')) for i in range(4)]
numeros = tuple(lista)

# Quantidade de números 9
print(f'\nNúmeros 9 armazenados: {numeros.count(9)}')

#Posição do primeiro 3
print(f'\nPosição do primeiro número 3: {numeros.index(3)}')

# Números pares
print('\nNúmeros pares digitados: ', end='')
for i in numeros:
    if i % 2 == 0:
        print(i, end=' ')
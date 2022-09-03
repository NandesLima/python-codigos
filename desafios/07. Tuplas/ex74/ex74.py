from random import sample

lista = sample(range(0,1000),5)
numeros = tuple(lista)

print('Números da tupla: ')
for i in numeros:
    print(i)

print(f'\nMaior: {max(numeros)}')
print(f'Menor: {min(numeros)}')
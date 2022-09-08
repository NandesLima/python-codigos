lista_numeros = [[],[]]
for i in range(7):
    numero = int(input(f'Digite o {i + 1}º número: '))
    if numero % 2 == 0:
        lista_numeros[0].append(numero)
    else:
        lista_numeros[1].append(numero)

lista_numeros[0].sort()
lista_numeros[1].sort()

print('Pares: ',end='')
for i in lista_numeros[0]:
    print(i, end=' ')

print('\nÍmpares: ',end='')
for i in lista_numeros[1]:
    print(i, end=' ')
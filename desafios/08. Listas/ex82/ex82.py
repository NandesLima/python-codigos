lista = list()
pares = list()
impares = list()

while True:
    numero = int(input('Digite um número: ').strip())
    lista.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
    sair = input('Digite N para sair: ').strip().upper()
    if sair == 'N':
        break

print(f'Todos os números: {lista}')
print(f'Pares: {pares}')
print(f'Ímpares: {impares}')
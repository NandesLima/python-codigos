lista_numeros = list()
count = 0
while True:
    count += 1
    numero = int(input(f'Digite o {count}º número: '))
    if numero in lista_numeros:
        print('Número já cadastrado')
    else:
        lista_numeros.append(numero)

    sair = input('Para parar a execução digite N: ').strip().upper()
    if sair == 'N':
        break

print('Números em ordem crescente: ',end='')
lista_numeros.sort()
for i in lista_numeros:
    print(i,end=' ')
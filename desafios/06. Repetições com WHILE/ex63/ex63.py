from time import sleep
base = 1
base2 = 1
while True:
    numero = int(input('Digite uma posição da sequência de fibonacci: '))
    if numero <= 0:
        print('Não existe posição nula ou negativa')
        sleep(0.7)
    else:
        break

i = 1
while (i <= numero):
    if i == 1:
        print(base2, end=' ')
    elif i == 2:
        print(base2, end=' ')
    else:
        soma = base2 + base
        base = base2
        base2 = soma
        print(base2, end=' ')
    i += 1

print(f'\nO {numero}° termo de fibonacci é {base2}')
numero = int(input('Digite um número inteiro: '))

count = 0
i = 0
for i in range (1, numero+1):
    if numero % i == 0:
        count += 1
    if count == 2:
        break

if i == numero:
    print('Número primo')
else:
    print('O número não é primo')
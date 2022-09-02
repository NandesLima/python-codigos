primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

print(f'PA: {primeiro_termo} ',end='')
i = 1
while (i < 10):
    primeiro_termo += razao
    print(primeiro_termo,end=' ')
    i += 1
print('...')
i = int(input('Quantos números deseja saber a mais: '))
count = 0
while (count < i):
    primeiro_termo += razao
    print(primeiro_termo, end=' ')
    count += 1
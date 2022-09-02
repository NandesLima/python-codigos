primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

print(f'PA: ',end='')
i = 0
while (i < 10):
    print(primeiro_termo+(i*razao),end=' ')
    i += 1
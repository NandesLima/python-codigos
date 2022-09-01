primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

print(f'PA: ',end='')
for i in range(10):
    print(primeiro_termo+(i*razao),end=' ')
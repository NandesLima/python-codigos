count = 0
soma = 0
while True:
    numero = int(input('Digite um número(999 para parar): '))
    if numero == 999:
        break
    else:
        count += 1
        soma += numero
print(f'Números usados: {count}')
print(f'Soma dos números: {soma}')
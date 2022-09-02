while True:
    valor = int(input('Digite o valor de saque: '))
    if valor <= 0:
        print('Digite um valor válido')
    else:
        break
quantidade = 0
if valor > 50:
    quantidade = valor//50
    valor -= quantidade*50
    print(f'Notas de 50: {quantidade}')
if valor > 20:
    quantidade = valor//20
    valor -= quantidade*20
    print(f'Notas de 20: {quantidade}')
if valor > 10:
    quantidade = valor//10
    valor -= quantidade*10
    print(f'Notas de 10: {quantidade}')
if valor > 1:
    quantidade = valor//1
    valor -= quantidade*1
    print(f'Notas de 1: {quantidade}')
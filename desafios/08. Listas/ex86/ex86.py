matriz = list()
tamanho = 0
for i in range(3):
    linha = []
    for j in range(3):
        numero = int(input(f'Digi o número da linha {i + 1} e da coluna {i + 1}: '))
        linha.append(numero)
        if i == 0 and j == 0 or len(str(numero)) > tamanho:
            tamanho = len(str(numero))
    matriz.append(linha)
print(tamanho)
for i in range(3):
    print('|',end=' ')
    for j in range(3):
        if len(str(matriz[i][j])) < tamanho:
            print(' '*(tamanho-len(str(matriz[i][j]))),end='')
        print(f'{matriz[i][j]}',end=' ')
    print('|')
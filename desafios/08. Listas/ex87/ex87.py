matriz = list()
tamanho = pares = terceira_coluna = 0
for i in range(3):
    linha = []
    for j in range(3):
        numero = int(input(f'Digi o número da linha {i + 1} e da coluna {i + 1}: '))
        linha.append(numero)
        # Tamanho dos espaços da matriz
        if i == 0 and j == 0 or len(str(numero)) > tamanho:
            tamanho = len(str(numero))
        # Pares
        if numero % 2 == 0:
            pares += numero
        # Terceira coluna
        if j == 2:
            terceira_coluna += numero
    matriz.append(linha)


for i in range(3):
    print('|',end=' ')
    for j in range(3):
        if len(str(matriz[i][j])) < tamanho:
            print(' '*(tamanho-len(str(matriz[i][j]))),end='')
        print(f'{matriz[i][j]}',end=' ')
    print('|')

print(f'''
Soma dos pares: {pares}
Soma dos valores da terveira coluna: {terceira_coluna}
Maior da segunda linha: {max(matriz[1])}''')
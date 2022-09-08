from operator import le


lista = list()
media = 0

while True:
    dados = []
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    media += dados[1]
    lista.append(dados)

    sair = input('Digite N para parar: ').strip().upper()
    if sair == 'N':
        break

media /= len(lista)
leves = list()
pesados = list()
for i in lista:
    if i[1] <= media:
        leves.append(i)
    else:
        pesados.append(i)

print(f'Pessoas cadastradas: {len(lista)}')
print(f'Pessoas pesadas: {pesados}')
print(f'Pessoas leves: {leves}')
maior1000 = 0
total = 0
preco_barato = 0
produto_barato = ''
continuar = 'E'

while continuar != 'N':
    # Dados do produto
    produto = input('Nome do produto: ')
    while True:
        preco = float(input('Preço do produto: R$ '))
        if preco <= 0:
            print('Escolha um preço válido')
        else:
            break
    
    # Análises
    total += preco
    if preco > 1000:
        maior1000 += 1
    if produto_barato == '' or preco < preco_barato:
        produto_barato = produto
        preco_barato = preco

    # Pergunta de continuar
    continuar = input('Para parar a execução digite N: ').strip().upper()

# Mostrando resultados
print(f'Produto mais barato: {produto_barato} R$ {preco_barato:.2f}')
print(f'Quantidade de produtos acima de R$ 1000,00: {maior1000}')
print(f'Total gasto: R$ {total:.2f}')
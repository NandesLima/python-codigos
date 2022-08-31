dias = int(input('Dias com o carro: '))
km_rodado = float(input('Quilômetros rodados: '))

valor = dias * 60 + km_rodado * 0.15

print(f'Valor do aluguel do carro: R$ {valor:.2f}')
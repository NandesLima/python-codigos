velocidade = float(input('Leitura da velocidade: '))

if velocidade > 80:
    print(f'Ultrapassou o limite de velocidade, a multa para {velocidade:.2f} km/h é de R$ {(velocidade-80)*7:.2f}')
else:
    print('Não ultrapassou o limite')
km_rodado = float(input('Digite os km rodados: '))

if km_rodado <= 200:
    print(f'Valor cobrado da viagem: R$ {km_rodado * 0.5:.2f}')
else:
    print(f'Valor cobrado da viagem: R$ {km_rodado * 0.45:.2f}')
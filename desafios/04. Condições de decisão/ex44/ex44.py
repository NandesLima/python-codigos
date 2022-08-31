valor = float(input('Digite o preço do produto: R$ '))

pagamento = int(input('''
1 - à vista ou cheque
2 - à vista no cartão
3 - em 2x no cartão (sem juros)
4 - 3x ou mais (com juros)

Escolha a opção: '''))

if pagamento == 1:
    print(f'\nValor R$ {valor * 0.9:.2f}')
elif pagamento == 2:
    print(f'\nValor R$ {valor * 0.95:.2f}')
elif pagamento == 3:
    print(f'''
Duas parcelas: R$ {valor/2:.2f}
Valor total: R$ {valor:.2f}
''')
elif pagamento == 4:
    parcelas = int(input('Escolha o número de parcelas: '))
    print(f'''
São {parcelas} parcelas: R$ {valor*1.2/parcelas:.2f}
Valor total: R$ {valor*1.2}
''')
else:
    print('Opção errada')
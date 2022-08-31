cidade = input('Digite o nome da cidade: ').strip().lower()
posicao = cidade.find('santo')

if posicao == 0:
    print('Início da frase')
elif posicao > 0:
    print(f'Localizado entre a posição {posicao + 1} e {posicao + 5}')
else:
    print('Não possui SANTO no nome')
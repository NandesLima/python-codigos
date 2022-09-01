from datetime import datetime
ano_atual = datetime.today().year
count = 0
for i in range(1, 8):
    nascimento = int(input(f'Digite o ano de nascimento do {i}° candidato: '))
    if ano_atual - nascimento >= 18:
        count += 1
        print('Maior de idade')
    else:
        print('Menor de idade')
print(f'Total de candidatos maiores de idade: {count}')
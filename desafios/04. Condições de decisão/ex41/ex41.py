from datetime import datetime

ano_atual = datetime.today().year
ano_nascimento = int(input('Data de nascimento: '))

idade = ano_atual-ano_nascimento

print(f'Sua idade é {idade}\nCategoria:', end=' ')

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 20:
    print('SÊNIOR')
else:
    print('MASTER')
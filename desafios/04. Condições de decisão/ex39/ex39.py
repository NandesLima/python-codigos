from datetime import datetime

ano_atual = datetime.now().year

nascimento = int(input('Digite sua data de nascimento: '))
idade = ano_atual-nascimento

if idade < 18:
    print(f'Você tem {idade} anos só precisa se alistar no ano {18 - idade + ano_atual}.')
elif idade == 18:
    print(f'Você tem {idade} anos, tem que se alistar esse ano.')
else:
    print(f'Você tem {idade} anos seu prazo de alistamento já passou, foi no ano {ano_atual - (idade - 18)}')
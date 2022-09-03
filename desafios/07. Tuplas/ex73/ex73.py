times = ('Palmeiras','Flamengo','Fluminense','Corinthias', 'Internacional', 'Athletico-PR', 
        'Athletico-MG', 'Santos','América-MG','Goiás','Bragantino','Fortaleza','São Paulo',
        'Botafogo','Ceará','Coritiba','Cuiabá','Avaí','Atlético-GO','Juventude')

print('5 Primeiros colocados')
for i in range(5):
    print(f'{i+1}° colocado: {times[i]}')

print('\n4 Últimos colocados')
for e in range(4,0,-1):
    print(f'{21-e}° colocado: {times[19-e]}')

print(f'\nPosição do Ceará: {times.index("Ceará")+1}° colocado')

lista = list(times)
lista.sort()

print('\nTimes em ordem alfabética: ')
for i in lista:
    print(i)

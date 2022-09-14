from random import randint
from time import sleep
from operator import itemgetter
from os import system

jogadores = dict()

# Guardando os valores
for i in range(4):

    system('cls')

    nome = input(f'Digite o {i+1}º nome: ').strip().capitalize()
    sleep(0.5)
    print('Jogando os dados')
    jogadores[nome] = randint(1,6)
    sleep(0.5)
    print(jogadores[nome])
    sleep(0.5)

# Organizando os valores
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

# Mostrando os valores
for i, e in ranking:
    print(f'{i:10}: {e}')

system('pause')
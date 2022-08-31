from random import choice
from time import sleep

nome1 = input('Digite o primeiro nome: ').capitalize().strip()
nome2 = input('Digite o segundo nome : ').capitalize().strip()
nome3 = input('Digite o terceiro nome: ').capitalize().strip()
nome4 = input('Digite o quarto nome  : ').capitalize().strip()

print('Sorteando um aluno')
sleep(0.5)
print(f'\033[35mO ALUNO SORTEADO FOI\033[m', end=' ')
sleep(0.5)
print(f'\033[32m{choice([nome1, nome2, nome3, nome4])}\033[m')
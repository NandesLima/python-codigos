from random import shuffle, sample
from time import sleep

nome1 = input('Digite o primeiro nome: ').capitalize().strip()
nome2 = input('Digite o segundo nome : ').capitalize().strip()
nome3 = input('Digite o terceiro nome: ').capitalize().strip()
nome4 = input('Digite o quarto nome  : ').capitalize().strip()

alunos = [nome1, nome2, nome3, nome4]

print('Organizando os alunos...')
sleep(0.5)
print(f'Utilizando a função sample: {sample(alunos, 4)}')
shuffle(alunos)
sleep(0.5)
print(f'Utilizando a função shuffle: {alunos}')

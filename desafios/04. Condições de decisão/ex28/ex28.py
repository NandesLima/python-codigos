from time import sleep
from random import randint
print(f'{"="*24} Jogo da Advinha {"="*24}')
sleep(0.5)
print('Vou pensar em um número entre 0 e 5 você tem que tentar advinhar')
sleep(0.5)
print('Está pronto? Aqui vou eu',end='')
for i in range(41):
    sleep(0.1)
    print('.',end='')
sleep(0.5)
sorteio = randint(0,5)
print('\nPronto já pensei em um número é a sua vez')
numero = int(input('Digite um número: '))
for i in range(65):
    sleep(0.1)
    print('.',end='')
print(' ')
if numero < 0 or numero > 5:
    print('Escolhendo um número que não está entre 0 e 5 você nunca vai vencer.')
elif numero == sorteio:
    print('Parabéns você acertou.')
else:
    print(f'Que pena o número que eu escolhi foi o {sorteio}')
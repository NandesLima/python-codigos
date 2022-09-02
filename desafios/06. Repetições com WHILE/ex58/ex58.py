from time import sleep
from random import randint
print(f'{"="*24} Jogo da Advinha {"="*24}')
sleep(0.5)
print('Vou pensar em um número entre 0 e 5 você tem que tentar advinhar')
sleep(0.5)
print('Está pronto? Aqui vou eu',end='')

count = 0

while True:

    for i in range(41):
        sleep(0.1)
        print('.',end='')
    sleep(0.5)
    sorteio = randint(0,5)
    print('\nPronto já pensei em um número é a sua vez')

    while True:
        numero = int(input('Digite um número: '))
        if numero < 0 or numero > 5:
            print('Você tem q escolher um número entre 0 e 5')
        else:
            break
    count += 1

    for i in range(65):
        sleep(0.1)
        print('.',end='')
    print(' ')
    if numero == sorteio:
        print('Parabéns você acertou.')
        break
    else:
        print(f'Que pena o número que eu escolhi foi o {sorteio}')
        print('Vamos de novo',end='')

print(f'Você venceu na {count}° partida')
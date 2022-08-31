from emoji import emojize
from time import sleep
from random import choice

computador = choice(['R', 'P', 'T'])

print('JOKENPO - PEDRA, PAPEL E TESOURA')
sleep(1)
print('Já escolhi minha opção, agora é sua vez...')

print(emojize('''
R - Pedra :black_circle:
P - Papel :page_facing_up:
T - Tesoura :scissors:
''', variant='emoji_type'))

jokenpo = input('Escolha uma das opções: ').strip().upper()


print('\nJO',end='')
sleep(0.7)
print('KEN',end='')
sleep(0.7)
print('PO',end='')
sleep(0.7)
print('.', end='')
sleep(0.7)
print('.', end='')
sleep(0.7)
print('.',)
sleep(1)

print(f'\n\nA minha opção foi {computador}')
print(f'\nA sua opção foi {jokenpo}')
print(f'\nEntão: ', end='')

if jokenpo == computador:
    print('Empate')
elif jokenpo == 'T' and computador == 'R':
    print('Eu venci')
elif jokenpo == 'T' and computador == 'P':
    print('Você venceu')
elif jokenpo == 'P' and computador == 'R':
    print('Você venceu')
elif jokenpo == 'P' and computador == 'T':
    print('Eu venci')
elif jokenpo == 'R' and computador == 'T':
    print('Você venceu')
elif jokenpo == 'R' and computador == 'P':
    print('Eu venci')
else:
    print('Você colocou uma opção errada.')
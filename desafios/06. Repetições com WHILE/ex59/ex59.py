from time import sleep

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))

while True:
    while True:
        numero = int(input('''
MENU
1 - Soma
2 - Multiplicar
3 - Maior
4 - Novos números
5 - Sair
        
Escolha uma das opções: '''))

        if numero < 1 or numero > 5:
            print('Escolha uma opção correta')
        else:
            break
    if numero == 1:
        print(f'{numero1} + {numero2} = {numero1 + numero2:.1f}')
    elif numero == 2:
        print(f'{numero1} x {numero2} = {numero1 * numero2:.1f}')
    elif numero == 3:
        if numero1 > numero2:
            print(f'''
Maior: {numero1:.1f}
Menor: {numero2:.1f}''')
        elif numero1 < numero2:
            print(f'''
Maior: {numero2:.1f}
Menor: {numero1:.1f}''')
        else:
            print('Ambos são iguais')
    elif numero == 4:
        numero1 = float(input('Digite o primeiro número: '))
        numero2 = float(input('Digite o segundo número: '))
    else:
        print('ATÉ MAIS')
        break
numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))

if numero1 > numero2:
    print(f'''
Maior: {numero1}
Menor: {numero2}
    ''')
elif numero1 < numero2:
    print(f'''
Maior: {numero2}
Menor: {numero1}
    ''')
else:
    print('\nValores iguais!')

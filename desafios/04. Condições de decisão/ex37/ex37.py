numero = int(input('Digite um número: '))

print('''
Menu
Escolha uma das seguintes opções
1 - Binário
2 - Octal
3- Hexadecimal''')

escolha = int(input())

if escolha == 1:
    print(f'Binário: {bin(numero)}')
elif escolha == 2:
    print(f'Octal: {oct(numero)}')
elif escolha == 3:
    print(f'Hexadecimal: {hex(numero)}')
else:
    print('Opção inválida')
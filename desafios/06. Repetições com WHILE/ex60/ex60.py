numero = int(input('Digite um núero: '))
fatorial = 1

while (numero > 1):
    print(numero, end=' * ')
    fatorial *= numero
    numero -= 1

print(f'1 = {fatorial}')
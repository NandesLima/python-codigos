peso = float(input('Digite o peso: '))
altura = float(input('Digige a altura: '))

imc = peso/(altura**2)

print(f'Seu IMC é {imc:.2f} você está ', end='')

if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc < 25:
    print('com PESO IDEAL')
elif imc < 30:
    print('com SOBREPESO')
elif imc < 40:
    print('com OBESIDADE')
else:
    print('com OBESIDADE MÓRBIDA')
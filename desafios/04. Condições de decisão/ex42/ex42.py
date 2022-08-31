reta1 = float(input('Qual o tamanho da primeira reta: '))
reta2 = float(input('Qual o tamanho da segunda reta: '))
reta3 = float(input('Qual o tamanho da terceira reta: '))

if reta3 < reta2 + reta1 and reta2 < reta3 + reta1 and reta1 < reta2 + reta3:
    if reta1 == reta2 and reta2 == reta3:
        print('Triângulo equilátero')
    elif reta1 == reta2 or reta3 == reta2 or reta1 == reta3:
        print('Triângulo isósceles')
    else:
        print('Triângulo escaleno')
else:
    print('Não forma um triângulo')
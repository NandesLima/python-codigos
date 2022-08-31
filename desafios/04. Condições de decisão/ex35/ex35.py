n1 = int(input('Digite o primeiro lado: '))
n2 = int(input('Digite o segundo lado : '))
n3 = int(input('Digite o terceiro lado: '))

if n1 > n2 + n3 or n2 > n1 + n3 or n3 > n2 + n1:
    print('Não forma um triângulo')
else:
    print('Forma um triângulo')
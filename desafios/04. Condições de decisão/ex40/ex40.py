nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2)/2

if media < 7:
    print(f'Sua média foi {media:.2F} - NÃO FOI APROVADO')
else:
    print(f'Sua média foi {media:.2F} - APROVADO')
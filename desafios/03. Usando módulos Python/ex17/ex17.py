import math

ca = float(input('Digite o Cateto Adjacente: '))
co = float(input('Digite o Cateto Oposto: '))

#Usando o método hypot
hipotenusa = math.hypot(ca, co)

#Calculando
hipotenusa2 = math.sqrt(pow(ca,2)+pow(co,2))

print(f'Hipotenusa usando a função hypot: {hipotenusa:.1f}')
print(f'Hipotenusa calculando: {hipotenusa2:.1f}')
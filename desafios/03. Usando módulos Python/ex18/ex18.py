from math import radians, sin, cos, tan

angulo = radians(float(input('Digite um angulo em graus: ')))

print(f'Seno    : {sin(angulo):.1f}')
print(f'Cosseno : {cos(angulo):.1f}')
print(f'Tangente: {tan(angulo):.1f}')
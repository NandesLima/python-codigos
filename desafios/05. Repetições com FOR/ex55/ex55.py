menor = 0.0
maior = 0.0
for i in range(1,6):
    peso = float(input(f'Digite o {i}° peso: '))
    if i == 1:
        menor = peso
        maior = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print(f'''
Menor peso: {menor:.2f}
Maior peso: {maior:.2f}
''')
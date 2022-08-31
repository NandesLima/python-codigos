maior = 0
menor = 0
for i in range(0,3):
    numero = int(input(f'Digite o {i+1} número: '))
    if i == 0 or numero > maior:
        maior = numero
    if i == 0 or numero < menor:
        menor = numero

print(f'Maior: {maior}')
print(f'Menor: {menor}')
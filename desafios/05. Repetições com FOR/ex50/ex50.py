soma_pares = 0
for i in range(1, 7):
    numero = int(input(f'Digite o {i}° número: '))
    if numero % 2 == 0:
        soma_pares += numero
print(f'A soma dos pares: {soma_pares}')
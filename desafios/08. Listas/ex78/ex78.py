lista_numeros = []
for i in range(5):
    numero = int(input(f'Digite o {i + 1}º número: ').strip())
    lista_numeros.append(numero)

print(f'Maior número: {max(lista_numeros)}, na {lista_numeros.index(max(lista_numeros))}ª posição')
print(f'Menor número: {min(lista_numeros)}, na {lista_numeros.index(min(lista_numeros))}ª posição')
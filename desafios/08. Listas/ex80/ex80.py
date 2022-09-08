lista_numeros = []

for i in range(5):
    numero = int(input(f'Digite o {i+1}º número: ').strip())
    if i == 0 or numero >= max(lista_numeros):
        lista_numeros.append(numero)
    else:
        for i,e in enumerate(lista_numeros):
            if numero>e:
                pass
            else:
                lista_numeros.insert(i,numero)
                break

    
print(lista_numeros)
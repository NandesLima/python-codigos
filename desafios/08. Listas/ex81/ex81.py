numeros = list()

while True:
    numero = int(input("Digite um número: ").strip())
    numeros.append(numero)
    sair = input('Para parar digite N: ').strip().upper()
    if sair == 'N':
        break

numeros.sort(reverse=True)
print(f'Números digitados: {len(numeros)}')
print(f'Lista decrescente: {numeros}')
print(f'O valor 5 foi digitado: {5 in numeros}')
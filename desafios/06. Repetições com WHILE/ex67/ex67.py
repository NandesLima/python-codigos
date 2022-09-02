while True:
    numero = int(input('Digite um número: '))
    if numero <= 0:
        break
    for i in range(1, 11):
        print(f'{numero} X {i:2} = {numero*i:2}')
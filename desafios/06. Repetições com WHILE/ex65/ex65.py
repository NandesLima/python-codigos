# Programa que ler vários números e a cada um perguntar se quer digitar um novo ou parar, ao final analise a média, o menor e maior valor.

soma = 0
count = 0
maior = 0
menor = 0

while True:
    count += 1
    numero = float(input('Digite um número: '))
    soma += numero
    if count == 1:
        maior = numero
        menor = numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    answer = input('Digite (N) para sair, qualquer outra coisa o programa continua: ').strip().upper()
    if answer == 'N':
        break

print(f'Maior: {maior:.1f}')
print(f'Menor: {menor:.1f}')
print(f'Média: {soma/count:.1f}')
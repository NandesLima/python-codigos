from time import sleep

maiores18 = 0
homens = 0
mulheres20 = 0
continuar = 'o'
while continuar != 'N':
    # Avaliando sexo
    while True:
        sexo = input('Digite o sexo (M/F): ').strip().upper()
        if sexo != 'M' and sexo != 'F':
            print('Digite M ou F')
            sleep(0.5)
        else:
            break
    # Avaliando idade
    while True:
        idade = int(input('Digite a idade: '))
        if idade < 0:
            print('Não existe idade negativa')
            sleep(0.5)
        else:
            break
    # Analisando os dados
    if idade >= 18:
        maiores18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    
    # Decidindo se quer continuar colocando os valores
    continuar = input('Para terminar a execução digite N: ').strip().upper()

# Mostrando o resultado
print(f'Homens: {homens}')
print(f'Pessoas maiores de 18: {maiores18}')
print(f'Mulheres menores de 20: {mulheres20}')
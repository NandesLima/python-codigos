# Programa tem que ler o nome, idade e sexo de 4 pessoas. E deve retorna a média de idade das pessoas, qual o nome do homem mais velho e quantas mulheres tem menos de 20 anos.
soma_idade = 0
mais_velho = ''
idade_mais_velho = 0
contar_mulher = 0
for i in range(1,5):
    nome = input(f'Digite o {i}° nome: ').strip().capitalize()
    sexo = input('Digite o sexo (M/F): ').strip().upper()
    idade = int(input('Digite a idade: '))
    soma_idade += idade
    if sexo == 'M' and (i == 1 or idade > idade_mais_velho):
        mais_velho = nome
        idade_mais_velho = idade
    if sexo == 'F' and idade < 20:
        contar_mulher += 1

print(f'''
Média de idade das pessoas: {soma_idade/4:.1f} anos
Homem mais velho: {mais_velho} com {idade_mais_velho} anos
Mulheres com menos de 20 anos: {contar_mulher}
''')
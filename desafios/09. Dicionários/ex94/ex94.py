from os import system

pessoas = list()
media = 0.0
mulheres = list()
acimaDaMedia = list()
continuar = 'S'
digitar = '''
Digite Nome, sexo e idade
Exemplo: Francisco M 12
Exemplo: Francisca F 13

=> '''

while continuar != 'N':

    dadosPessoais = dict()
    # Validação de dados
    while True:
        system('cls')
        # Digitar o nome, sexo e idade em uma linha só
        dados = input(digitar).strip().split()
        # Validação do formato da entrada
        if len(dados) != 3:
            print('\nDigite conforme o exemplo.\n')
            system('pause')
        # Validação do sexo
        elif dados[1].upper() not in 'MF':
            print('\nDigit M para Masculino e F para Feminino\n')
            system('pause')
        # Validação da idade
        elif not dados[2].isnumeric():
            print('\nA idade deve ser um número inteiro\n')
            system('pause')
        else:
            break
    # Cadastrando dados no dicionário
    dadosPessoais['nome'] = dados[0].capitalize()
    dadosPessoais['sexo'] = dados[1].upper()
    dadosPessoais['idade'] = int(dados[2])

    # Somando idades
    media += dadosPessoais['idade']

    # Cadastrando dados na lista
    pessoas.append(dadosPessoais)

    # Condição de saída
    continuar = input('Digite N para não cadastrar mais: ').strip().upper()

# Definindo média
media /= len(pessoas)

# Validação dos dados de saída
for i in pessoas:
    if i['sexo'] == 'F':
        mulheres.append(i['nome'])
    if i['idade'] > media:
        acimaDaMedia.append(i['nome'])

system('cls')
# Mostrando saídas
print(f'''
Pessoas cadastradas  : {len(pessoas)}
Média das idades     : {media:.2f}
Mulheres cadastradas : {mulheres}
Acima da idade média : {acimaDaMedia}
''')
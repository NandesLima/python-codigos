from datetime import datetime
from os import system

anoAtual = datetime.now().year
dadosTrabalho = dict()

continuar = 'ENTRAR'

while 'SAIR' not in continuar and 'S' not in continuar:

    system('cls')
    # Cadastro de dados
    # Nome
    nome = input('Nome: ').strip().capitalize()
    dadosTrabalho[nome] = dict()

    # Nascimento e idade
    nascimento = 0
    while nascimento >= anoAtual or nascimento <= (anoAtual-150):
        nascimento = int(input('Ano de nascimento: '))
        if nascimento >= anoAtual or nascimento <= (anoAtual-150):
            print('Digite um ano válido')
            continue
        dadosTrabalho[nome]['nascimento'] = nascimento
        dadosTrabalho[nome]['idade'] = anoAtual - nascimento

    # Carteira de trabalho, contratação e aposentadoria
    carteira = int(input('Números CTPS: '))
    dadosTrabalho[nome]['ctps'] = carteira
    if carteira > 0:
        anoContratacao = 0
        # Cadastrando ano de contratação considerando idade mínima de 16 anos
        while not nascimento + 16 <= anoContratacao <= anoAtual:
            anoContratacao = int(input('Ano de contratação: '))
            if not nascimento + 15 <= anoContratacao <= anoAtual:
                print('Digite um ano válido')
                continue
            dadosTrabalho[nome]['contratação'] = anoContratacao
            dadosTrabalho[nome]['aposentadoria'] = anoContratacao + 35

    # Condição de saída
    continuar = input('Digite SAIR ou S para sair: ').strip().upper()
    if continuar != 'S' and continuar != 'SAIR':
        continue
    print('\n')
    system('pause')

# Cabeçalho
system('cls')
print(f'{"Nome":^15}\t{"Nascimento"}\t{"Idade":^10}\t{"CTPS":^10}\t{"Contrata.":^10}\t{"Aposenta.":^10}')
print('-'*90)

# Mostrando dados de forma tabular
for i, e in dadosTrabalho.items():
    print(f'{i:^15}',end='\t')
    for n in e.values():
        print(f'{n:^10}',end='\t')
    print()
from cgi import print_arguments
from os import system

alunos = dict()
sair = ''

while sair != 'S':
    # Limpeza dos dados
    system('cls')

    # Guardando dados dos alunos
    nome = input('Nome: ').strip().capitalize()
    alunos[nome] = dict()
    alunos[nome]['Nota1'] = float(input('Primeira nota: '))
    alunos[nome]['Nota2'] = float(input('Segunda nota : '))
    alunos[nome]['Média'] = (alunos[nome]['Nota1'] + alunos[nome]['Nota2'])/2
    alunos[nome]['Status'] = 'Aprovado' if alunos[nome]['Média'] >= 7 else 'Reprovado'

    sair = input('Digite S para não guardar mais valores: ').strip().upper()

# Cabeçalho
system('cls')
print(f'\n{"Aluno":^10}\t{"Nota 1":^8}\t{"Nota 2":^8}\t{"Média":^8}\t{"Status":^8}')
print('-'*73)

# Organização dos dados
for e, i in alunos.items():
    print(f'{e:^10}',end='\t')
    for n in i.values():
        print(f'{n:^8}',end='\t')
    print()
print('\n')
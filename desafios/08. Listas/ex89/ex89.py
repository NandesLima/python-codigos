from os import system
turma = [['Nome','Nota1','Nota2','Média','Status']]
sair = 'O'
while sair != 'N':
    system('cls')
    aluno = []
    notas = []
    aluno.append(input('Nome: ').strip().capitalize())
    for i in range(2):
        notas.append(float(input(f'Digite a {i + 1}ª nota: ')))
    aluno.append(notas)
    aluno.append(sum(notas)/2)
    if aluno[2] >= 7:
        aluno.append('Aprovado')
    else:
        aluno.append('Reprovado')
    turma.append(aluno)

    sair = input('Digite N para sair: ').strip().upper()

system('pause')
system('cls')

resposta = 'S'

while resposta == 'S':
    system('cls')
    nome = input('Pesquisar aluno: ').strip().capitalize()
    for m in turma:
        if m[0] == nome:
            for i, e in enumerate(turma[0]):
                if i == 0:
                    print(f'{e:15}\t',end='')
                else:
                    print(f'{e}\t',end='')
            print()
            for e, j in enumerate(m):
                if e == 0:
                    print(f'{j:15}\t',end='')
                elif e == 1:
                    for n in j:
                        print(f'{n}\t',end='')
                elif e == 2:
                    print(f'{j}\t',end='')
                else:
                    print(j)
    resposta = input('Para verificar novos alunos digite S: ').strip().upper()
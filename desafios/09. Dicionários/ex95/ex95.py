from os import system

menu ='''--------------------------------
Pesquisar dados de um jogador 
específico:

Digite o nome do jogador
ou
N para encerrar
--------------------------------
=> '''

jogadores = {}
cadastrar = 'S'
pesquisa = 'S'

while cadastrar == 'S':
    system('cls')
    nome = input('Nome: ').strip().capitalize()
    jogadores[nome] = dict()
    jogadores[nome]['jogos']= int(input('Número de jogos: '))
    jogadores[nome]['gols'] = dict()
    soma = 0
    for i in range(jogadores[nome]['jogos']):
        jogo = f'{i+1}º jogo'
        jogadores[nome]['gols'][jogo] = int(input(f'Gols {jogo}: '))
        soma += jogadores[nome]['gols'][jogo]
    jogadores[nome]['media'] = soma/jogadores[nome]['jogos']

    cadastrar = input('Digite S para cadastrar novo jogador: ').strip().upper()


while pesquisa != 'N':
    system('cls')
    print(f'{"Nome":^15}\tJogos\tMédia')
    print('-'*32)
    for i, e in jogadores.items():
        print(f'{i:^15}',end='\t')
        print('{jogos:^5}\t{media:^5.2f}'.format(**e))

    pesquisa = input(menu).strip().capitalize()
    if pesquisa == 'N':
        continue
    elif pesquisa not in jogadores.keys():
        print('Jogador não encontrado\n')
        system('pause')
    else:
        print(f'Nome     :\t{pesquisa}')
        print(f'Jogos    :\t{jogadores[pesquisa]["jogos"]}')
        soma = 0
        for i in jogadores[pesquisa]["gols"]:
            print(f'{i:9}:\t{jogadores[pesquisa]["gols"][i]}')
            soma += jogadores[pesquisa]["gols"][i]
        print(f'Total    :\t{soma}')
        print(f'Média    :\t{jogadores[pesquisa]["media"]:.2f}')
        system('pause')
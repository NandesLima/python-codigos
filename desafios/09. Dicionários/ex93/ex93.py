from os import system

jogadores = {}
cadastrar = 'S'

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

system('cls')
print(f'{"Nome":^15}\tJogos\tMédia')
print('-'*32)
for i, e in jogadores.items():
    print(f'{i:^15}',end='\t')
    print('{jogos:^5}\t{media:^5.2f}'.format(**e))
print()

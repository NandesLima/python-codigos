from random import sample

quantidade = int(input('Quantidade de jogos: '))

for i in range(quantidade):
    jogo = sample(range(1,60),6)
    jogo.sort()
    print(f'{i+1}º jogo: {jogo}')
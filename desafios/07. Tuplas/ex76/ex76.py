produtos = ('Arroz', 3.50, 'Feijão', 9.75, 'Chocolate', 6.78, 'Gelo', 6.0)

for i, e in enumerate(produtos):
    if i % 2 == 0:
        print(f'{e:10}',end='')
    else:
        print(f'\t{e:.2f}')
palavras = ('Ernandes', 'teste', 'DIO', 'Nayra', 'Aprender praticando', 'Never Stop Learning')
print(f'{"Palavras":20}\tVogais\n')
for i in palavras:
    print(f'{i:20}',end='\t')
    for j in i:
        if j.lower() in 'aeiou':
            print(j,end=' ')
    print('')

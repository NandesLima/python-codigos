soma = 0
count = 0
for i in range (0, 500, 3):
    if i % 2 != 0:
        print(f'{i:3}', end=' ')
        soma += i
        count += 1
    if count == 20:
        print('\n')
        count = 0
print(f'= {soma}')
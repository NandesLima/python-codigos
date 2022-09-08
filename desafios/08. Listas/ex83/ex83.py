parenteses = 0
expressao = input('Digite uma expressão: ')
for i in expressao:
    if i == '(':
        parenteses += 1
    if i == ')':
        parenteses -= 1
    if parenteses <= -1:
        break

if parenteses == 0:
    print('Parenteses abertos na ordem correta')
else:
    print('Parenteses não estão na ordem correta')

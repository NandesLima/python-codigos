nome = input('Digite seu nome completo: ').strip().title()

nome2 = nome.split(' ')

nome = nome2[0] + ' ' + nome2[-1]

print(nome)

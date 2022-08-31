a = input('Digite alguma coisa: ')

print(f'{a} - é alfanumérico: {a.isalnum()}')
print(f'{a} - são apenas letras: {a.isalpha()}')
print(f'{a} - está tudo em letras minúsculas: {a.islower()}')
print(f'{a} - é um número: {a.isnumeric()}')
print(f'{a} - são somente espaços: {a.isspace()}')
print(f'{a} - somente a primeira letra é maiúscula: {a.istitle()}')
print(f'{a} - todas as letras são maiúsculas: {a.isupper()}')
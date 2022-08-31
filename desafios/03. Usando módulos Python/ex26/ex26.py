palavra = input('Digite uma palavra: ').strip().upper()
letra = input('Escolha uma letra: ').upper()

print(f'Quantidade de vezes que a letra {letra} aparece: {palavra.count(letra)}')
print(f'Primeira ocorrência da letra {letra} é na posição: {palavra.find(letra) + 1}')
print(f'A última ocorrência da letra {letra} é na posição: {palavra.rfind(letra) + 1}')
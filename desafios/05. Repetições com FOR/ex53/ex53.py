frase = input('Digite uma frase: ').strip().lower()
frase = frase.split()
frase = ''.join(frase)
frase_inversa = frase[::-1]

if frase == frase_inversa:
    print('Essa frase é um palíndromo')
else:
    print('Essa frase não é um palíndromo')

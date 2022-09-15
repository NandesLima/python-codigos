print('Teste') # Imprime na tela o que estiver entre parênteses

n = 'Novo texto'
m = ' Mais um texto'

print(n + m) # O + consegue juntar textos
print(n , m, 75) # A vírgula consegue juntar textos e números
print('=' * 30) # A mutiplicação serve para repetir os caracteres de um texto

print(f'Teste: {n}') # fprint f antes das aspas faz com que seja possível utilizar variáveis dentro do print.
print('Teste: {}'.format(n)) # .format() é um método que funciona como o fprint.

print('Teste',end='-') # Parâmetro end muda o último caractere da função print (\n)
print('\n')
print(n, m, sep="-") # Sep muda os separadores que por padrão é o espaço por outro caractere

print('\033[35;44;4mTeste\033[m') # \033[estilo;cor do texto;cor de fundom --> Muda o estilo do texto
# Base: \033[m
# Estilos: 0 1 2 3 4 5 6 7
# Cor do texto: 30 31 32 33 34 35 36 37 38 39
# Cor de fundo: 40 41 42 43 44 45 46 47 48 49

n = 'Novo texto teste'
print("{:20}".format(n)) # Coloca a quantidade mínima de caracteres igual o valor depois dos :, se for colocado menos caracteres é preenchido com oputro, se não for escolhido um é utilizado o espaço.
print(f'{n:20}') # Funciona da mesma forma que o .format()

print(f'{n:>20}') # Alinha para a direita
print(f'{n:<20}') # Alinha para a esquerda (posição normal)
print(f'{n:^20}') # Alinha ao centro
print(f'{n:=<20}') # Define o caractere a ser utilizado e alinha à esquerda
print(f'{n:~^30}') # Define o caractere a ser utilizado e alinha ao centro
print(f'{n:+>40}') # Define o caractere a ser utilizado e alinha à direita

m = 4.7586989895269494156

print(f'{m:.2f}') # Define a quantidade de casas deciamis após o ponto flutuante

m = n.isspace() # Retorna um booleano se a String tiver somente espaços
u = n.isupper() # Retorna um booleano se a String tiver somente letras maiúsculas
p = n.istitle() # Retorna um booleano se a String tiver somente a primeira letra maiúscula
q = n.islower() # Retorna um booleano se a String tiver todas as letras em minúsculo
r = n.isnumeric() # Retorna um booleano se a String tiver apenas números
s = n.isalpha() # Retorna um booleano se a String tiver apenas letras
t = n.isalnum() # Retorna um booleano se a String tiver letras e números

print("teste"[2]) # Retorna o caractere da posição indicada
print(n[2:8]) # Retorna todos os caracteres entre o primeiro e o segundo número
print(n[3:12:2]) # O terceiro número indica o salto, ou seja de quantos em quantos números ele conta pra considerar o próximo caractere
print(n[3:]) # Retorna todos os caracteres a partir do primeiro indicado
print(n[:12]) # Retorna todos os caracteres antes do último indicado
print(n[3::2]) # Retorna os caracteres contando a cada salto depois do inicial indicado
print(n[:12:2]) # Retorna todos os caracteres a cada salto antes do final indicado
print(n[::2]) # Retorna os caracteres considerando o salto
print(n[::-1]) # Retorna o texto invertido, já que o salto é -1

print(n.count('te')) # Conta quantas vezes um caractere ou sequência se repetem.
print(n.count('te',6,-3)) # Conta quantas vezes se repete considerando a primeira posição indicada e a última posição indicada, pode se utilizar apenas a inicial também.
print(n.count('te',6))

print(n.find('te')) # Mostra a primeira ocorrência do caractere ou sequÊncia de caracteres
print(n.find('te', 6)) # Mostra a ocorrÊncia contando a partir da posição indicada
print(n.rfind('te')) # Mostra a primeira ocorrência a partir da direita

print('texto' in n) # Retorna o booleano considerando se o texto da esquerda está contido no da direita

n = n.replace('texto', 'guitarra') # Troca o primeiro texto pelo segundo dentro de uma String

print('teste'.upper()) # Transforma todas as letras em maiúsculas
print('TESTE'.lower()) # Transforma todas as letras em minúsculo
print(n.capitalize()) # Primeira letra de cada palavra fica maiúscula
print(n.title()) # Apenas a primeira letra fica maiúscula

o = "       teste       "
print(o.strip()) # Retira todos os espaços a esquerda e à direita do texto
print(o.rstrip()) # Retira todos os espaços à direita do texto
print(o.lstrip()) # Retira todos os espaços à esquerda do texto

o = n.split() # Separa as palavras por um caractere indicado, quando não se indica é utilizado o espaço, e salva as palavras separdas em uma lista.
a = n.split('ta')
b = n.rsplit() # Separa as palavras pela direita

n = '-'.join(b) # Junta os itens de uma lista numa String, com o caractere indicado antes do ponto
c = ''.join(b) # Pode ser juntado sem nenhum caractere

print(len(c)) # Mostra quantos caracteres tem a String, ou quantos elementos tem uma lista.

d = input('Digite algo: ') # Permite que o usuário insira pelo teclado um valor
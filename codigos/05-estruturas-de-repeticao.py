# Comando range
lista = range(5) # Cria uma lista de números a parir do 0 até o anterior do indicado.
nova_lista = range(1, 6) # Cria uma lista a partir do primeiro número, até um número antes do indicado.
new_lista = range(1,20,2) # Vai aumentando conforme o terceiro número, funciona como um passo.
lista_contraria = range(20,0,-1) # O passo é negativo nesse caso

# Comando enumerate
lista2 = enumerate(lista_contraria) # Cria uma lista de posições para cada elemento de um sequência e associa ambos em uma tupla

# Estrutura de repetção FOR
for i in lista: # O for sempre deve está associado a uma ou mais suquências, a variável recebe cada valor da sequência
    print(i)

for i, j in lista2: # Como pra cada elemento da lista, existem dois itens, pode utilizar uma variável para cada item que deseja guardar o valor.
    print(i, j)

lista_for = [i+2 for i in new_lista] 
# O for pode ser utilizado para criar listas de uma forma mais rápida
# Antes do for fica o valor que vai ser armazenado na lista
# Depois do for fica a variável
# Depois do in fica a sequência que o for terá que percorrer

print(lista_for)

# Estrutura de repetição WHILE
n = 0
while n < 10: #  Executa os comando internos enquanto a condição for verdadeira
    print(n)
    n += 1

while True:
    print(n)
    n+=1
    if n == 30:
        break # Para a execução de uma estrutura de repetição, serve para o for e para o while

senha = ''

while senha != 'teste123':
    senha = input('Digite a senha: ')
    if senha != 'teste123':
        continue # Quando executado ele desconsidera todo o restante abaixo dele dentro do laço, e volta para o início do loop
    print('Acesso liberado')
n = 100

if n < 100:
    print('Executa if')
elif n < 200:
    print('Executa elif')
elif n < 400:
    print('Executa elif')
else:
    print('Executa else')

if n > 80:
    print('Teste if')
else:
    print('Teste else')

if n <= 90 and n >= 70: # Uso do conectivo e
    print('Mais um teste de if')

if 70<=n<=90: # No python pode utilizar o conectivo and dessa forma
    print('Igual ao de cima')

if n <= 70 or n >=100: #Uso do conectivo ou
    print('Teste do conectivo ou')

if not n <= -50: # Uso da negação lógica
    print('Teste da negação lógica')

# Dentro do if e do elif são analisadas condições que retornam em valores booleanos, caso o valor retornado seja True no if ou elif, será executado o comando interno
# Se o if for escolhido os demais não serão, caso não seja passa para o próximo.
# Se um elif for escolhido não executa os demais, caso não seja passa para o próximo.
# Não é necessário utilizar elif ou else

# Os comparativos matemáticos são utilizados aqui
# > --> maior que
# < --> menor que
# == ---> igual a
# != ---> diferente de
# >= ---> Maior ou igual
# <= ---> menor ou igual

if str(n) in '907080':
    print('Testando se está dentro de um conjunto')

print(n if n <= 200 else n+200) # Pode ser utilizado o if e o else numa linha dessa forma
# Antes do if fica o valor retornado se a condição for verdadeira
# Entre o if e o else fica a condição
# Depois do else fica o valor retornado se a condição for falsa
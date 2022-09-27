
try:  # Faz o teste do programa para verificar se há erros
    numero1 = float(input('Digite o primeiro número: '))
    numero2 = float(input('Digite o segundo número: '))

    divisao = numero1/numero2
except ZeroDivisionError: # Caso tenha uma erro retorna o que tem dentro da excessão, a excessão pode ser conhecida ou não.
    print('Não se pode fazer divisão por zero')
except:
    pass # Serve para se colocar num código para não ficar vazio

print('https://docs.python.org/pt-br/3.10/library/exceptions.html#bltin-exceptions') # Lista de Excessões
# As exceções possuem uma hierarquia, e as vezes várias podem estar dentro da mesma classe
# BaseException é a maior hierarquia

try:
    numero = int(input('Digite um número: '))
except BaseException as excessao: # Guarda uma excessão que seja parte da hierarquia dentro da variável
    print(excessao.__class__) # Retorna a classe do objeto
else: # O else pode ser utilizado quando uma excessão não aparece
    print(numero)
finally: # Executa mesmo que o erro seja executado ou não
    print('Parabéns!!!')


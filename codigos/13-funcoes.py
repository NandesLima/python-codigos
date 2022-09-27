# Funções

def nova_funcao ():   # Função sem parâmetros e sem retornar um valor
    for i in range(2):
        print('Teste da função')

def soma():
    quantidade = int(input('Digite a quantidade de números: '))
    soma = 0
    for i in range(1, quantidade+1):
        numero = int(input(f'Digite o {i}º número: '))
        soma += numero
    
    return soma # Return faz com que a função retorne um valor no final da execução

def soma_2(numero1, numero2): # Utilização de parâmetros dentro da função
    return numero1 + numero2

def soma_3(*numero): # O parâmetro que recebe *, utiliza mais de um valor, ou seja, pode utilizar uma ou mais variáveis do mesmo tipo, os valores são guardados em uma tupla
    soma = 0
    for i in numero:
        soma += i
    return soma

def soma_4(*numero2, numero1=0): # O parâmetro quando já recebe um valor, começa com esse valor associado, mas pode ser utilizado um valor diferente
    for i in numero2:
        numero1 += i
    return numero1

def print_info (**dicionario): # ** Esse parâmetro cria um dicionário nos valores
    print(dicionario,  type(dicionario))

# Recursividade

def fatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * fatorial(numero - 1) # Recursividade é quando uma função é chamada dentro dela mesmo
                                             # Toda função recursiva deve ter um critério de parada, para evitar um loop infinito

def fibonacci(numero):
    if numero == 0 or numero == 1:
        return numero
    else:
        return fibonacci(numero-1) + fibonacci(numero-2)


# Retornando funções 
if __name__ == '__main__': # Executa os códigos direto do arquivo onde estão, no caso de serem importadas não são executadas
    nova_funcao() # Para chamar a função criada é só colocar o nome colocado após o def, se tiver parâmetros colocar entre parâmetros.
    print(soma())
    print(soma_2(12,13))
    print(soma_3(10,9,8,7,6,5,3,2,1))
    print(soma_4(4,5,5,5,6,numero1=12))
    print_info(nome='Angelo',sobrenome='Bardy',idade=32) # Sempre deve definir o parâmetro que será guardado aqui e o valor associado, o parâmetro é retornado como uma chave e o valor como seu valor associado, tudo dentro de um dicionário


    # Função anônima - Lambda
    
    soma_5 = lambda numero1, numero2: numero1 + numero2 # Lambda cria uma função sem nome (anônima), os parâmetros são colocados antes dos dois pontos
                                                        # as intruções de execução da função são colocadas após os dois pontos
                                                        # A função é guardada dentro de uma variável
    
    print(soma_5(10,12)) # Os parâmetros são colocados na variável quando chamá-la

    dicionario = {'mutiplicar': lambda numero1,numero2: numero1 * numero2, # A função lambda é últil para guardar várias funções em um dicionário
                  'somar'     : lambda numero1,numero2: numero1 + numero2,
                  'diminuir'  : lambda numero1,numero2: numero1 - numero2}
    
    print(dicionario['diminuir'](22,10))
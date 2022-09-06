import random # Importa um módulo de valores aleatórios

lista = ['Valor1','Valor2','Valor3','Valor4','Valor5']

numero = random.random() # Gera um float aleatório entre 0 e 1
numero1 = random.randint(10,101) # Escolhe um número aleatório entre o primeiro e o segundo número
aleatorio = random.choice(lista) # Escolhe aleatóriamente um valor da lista
lista_aleatoria = random.sample(lista,2) # Sorteia de forma aleatória a quantidade de elementos da lista, indicada no segundo parâmetro
random.shuffle(lista) # Embaralha os elementos da lista

print(lista)
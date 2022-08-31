# Biblioteca voltada para matemática
import math

numeros = [1, 5, 7, 2, 100, -5, 15, 13, -38, 0]

print(abs(-4.38)) # Retorna o valor absoluto de um número
print(round(4.75)) # Arredonda o valor de um núemro
print(sum(numeros)) # Soma uma lista de números
print(min(numeros)) # Retorna o menor valor de uma lista de números
print(max(numeros)) # Retorna o maior valor de uma lista de números
print(pow(4,2)) # Funciona como uma exponenciação onde o primeiro número é a base e o segundo é o expoente.

print(2 + 2) # + --> Usado pra soma
print(3 - 1) # - --> Usado pra subtração
print(4 * 2) # * --> Utilizado para mutiplicação
print(6 / 3) # / --> Utilizado para divisão
print(2 ** 3) # ** Utilizado para exponenciação
print(5 % 2) # % Retorna o resto de uma divisão
print(10 // 3) # // Retorna o valor inteiro de uma divisão

n = 10
n += 1 # Serve para somar com a própria variável
n -= 2 # Serve para diminuir com a própria variável
n *= 3 # Mutiplica com a variável
n //= 4 # Calcula a divisão inteira da própria variável
n **= 2 # Calcula a exponencial da própria variável
n /= 4 # Calcula a diisão da própria variável
n %= 2 # Calcula o resto da divisão da própria variável

print(math.sqrt(9)) # Calcula a raiz quadrada
print(math.ceil(4.32)) # Arredoda o valor para cima
print(math.floor(4.78)) # Arredonda o valor para baixo
print(math.trunc(4.999999)) # Retorna a parte inteira
print(math.hypot(3,4)) # Retorna a hipotenusa dos dois catetos colocados
n = math.radians(30) # Transforma o ângulo de graus para radiano
print(math.sin(n)) # Retorna o seno de um número que esteja em radiano
print(math.cos(n)) # Retorna o cosseno de um número que esteja em radiano
print(math.tan(n)) # Retorna a tangente de um número que esteja em radiano


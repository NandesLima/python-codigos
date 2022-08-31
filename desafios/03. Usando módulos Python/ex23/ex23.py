numero = int(input('Digite um número de 0 a 9999: '))
u = numero // 1 % 10 # Divide o número por 1 e retorna apenas a parte inteira, depois divide a parte inteira por 10 e retorna o resto, que será a unidade.
d = numero // 10 % 10 # Divide o número por 10 e retorna a parte inteira, depois divide por 10 e retorna o resto que será igual as desenas.
c = numero // 100 % 10 # Divide o número por 100 e retorna a parte inteira e depois divide por 10 e retorna o resto que é igual a centena.
m = numero // 1000 % 10 # Divide o número por 1000 que retorna a parte inteira e depois divide por 10 e retorna o resto que é igual ao milhar.

print(f'''
Unidade: {u}
Dezena : {d}
Centena: {c}
Milhar : {m}
''')
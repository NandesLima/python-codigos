arquivo = open('11-teste.txt','w') # Abre um arquivo, com o nome e formato colocado no primeiro parâmetro e a ação no segundo parâmetro
                                   # O arquivo é associado a uma variável e quando aberto dessa forma precisa do método .close() para fechar o arquivo
# Tipos de ações
# 'w' --> Permite a abertura do arquivo para escrever ou sorbreescrever o arquivo
# 'r' --> Permite a abertura do arquivo para leitura
# 'a' --> Permite a abertura do arquivo no modo append, pemite concatenar nvos conteúdos
# 'x' --> Permite a abertura do arquivo no modo exclusivo
# 't' --> Permite a abertura do arquivo com o conteúdo como string
# 'b' --> Permite a abertura do arquivo com o conteúdo em binário

# Podem ser utilizadas mais de uma palavra

arquivo.write('Conteúdo interno\n') # Escreve o conteúdo interno no arquivo
arquivo.write('Segunda linha\n')
arquivo.close() # Fecha o arquivo

# O as é utilizado para apelidar um objetivo, pode ser utilizado inclusive na importação de bibliotecas
# Exemplo: import math as m, toda vez que retornar m retornará a biblioteca math

with open('11-teste.txt','r') as arquivo: # Abre o arquivo associa e o apelida/associa a uma variável mas não precisa do método .close() para ser fechado
    print(arquivo.read()) # Faz a leitur do arquivo

novo_arquivo = open('11-teste.txt','r')
linha = ' '
while linha != '':
    print(linha, end='')
    linha = novo_arquivo.readline() # Lê apenas uma linha por vez, o método mexe com o cursor do Python, então toda vez que for executado mostrará uma linha diferente
arquivo.close()

novo_arquivo = open('11-teste.txt','r')
for linha in novo_arquivo: # Cada linha vai ser considerada separada durante a execução do for
    print(linha, end='')
arquivo.close()

novo_arquivo = open('11-teste.txt','r') # Codificação padrão
print(novo_arquivo.readlines()) # Cria uma lista onde cada elemento é uma linha do arquivo
arquivo.close()

novo_arquivo = open('11-teste.txt','r')
print(novo_arquivo.readlines()[1:]) # A manipulação funciona igual ao de strings
arquivo.close()

with open('11-teste.txt','a') as arquivo: # Nesse caso ele continua a partir do final do cursor no arquivo existente
       arquivo.write('Terceira linha\n')

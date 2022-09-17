import csv # Biblioteca própria para manipulação de arquivos .csv

dados = [['Maria', 'Sertão', 'maria@email.com', 'Feminino'],['Fatima', 'Isolda', 'fatima@email.com', 'Feminino']]

with open('11-teste.csv', 'w', newline='') as arquivo_csv: # O parâmetro newline troca o \n no final de cada nova linha pelo caractere selecionado
    escritor = csv.writer(arquivo_csv) # Permite escrever no modo CSV
    escritor.writerow(['nome', 'sobrenome', 'e-mail', 'genero']) # Escreve toda uma linha no arquivo CSV, da mesma forma que ele retorna valores como lista, tem que passar os valores como uma lista
    escritor.writerow(['Angelo', 'Bardy', 'angelobardy@email.com', 'Masculino']) # A cada linha o Python por padrão adiciona uma quebra de linha
    escritor.writerow(['Francisco', 'Elias', 'franelias@email.com', 'Masculino'])
    escritor.writerows(dados) # Adiciona mais de uma linha

with open ('11-teste.csv', 'r') as arquivo_csv:
    leitor = csv.reader(arquivo_csv) # Cada linha se torna uma lista com seus elementos separados
    cabecalho = next(leitor) # Ignora um das interações do arquivo, pode guardar ou não a interação guardada
    for linha in leitor:
        print(linha)
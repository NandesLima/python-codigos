import shutil # Módulo de manipulação de arquivos

shutil.copy('teste.txt','modulos/novo_teste.txt') # Copia o arquivo inicial e coloca em um novo dicionário, com um novo nome
shutil.copy('teste.txt','modulos/') # Sem um novo nome o anterior permanece
shutil.copy('teste.txt','novo_teste.txt') # Sem colocar um diretório a cópia é feita no diretório atual

shutil.move('teste.txt', 'modulos/novo_teste.txt') # Move o arquivo inicial para um novo dicionário, com um novo nome
shutil.move('teste.txt', 'modulos/') # Sem um novo nome o anterior permanece

import os # Acessa objetos e funções que mexem no sistema operacional

print(os.path.exists('teste.txt')) # Verifica se existe um determinado arquivo


limpar = 'cls' # Comando de limpar a tela do windows (shell)
limpar = 'clear' # Comando de limpar a tela do linux (unix/bash)

pausar = 'pause' # Pausa a execução no windows (shell)
pausar = 'read -p "Precione ENTER para continuar..."' # Pausa a execução no linux (unix/bash)
# read métodode de leitura do bash, aguarda precionar ENTER para continuar
# -s modo silencioso, aguarda qualquer tecla ser precionada, mas não guarda o seu valor
# -r coloca no modo rudimentar necessário para que considere teclas como /
# -p especifica o prompt

os.system(pausar) # Pausa o programa até ter uma tecla ser precionada e o programa continua
os.system(limpar) # Limpa a tela do terminal no Linux

# O método .system() utiliza comandos do terminal
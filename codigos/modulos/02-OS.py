from msilib import PID_TITLE
import os # Acessa objetos e funções que mexem no sistema operacional

print(os.path.exists('teste.txt')) # Verifica se existe um determinado arquivo
os.system('pause') # Pausa o programa até ter uma tecla ser precionada e o programa continua
os.system('cls') # Limpa a tela do terminal
# O método .system() acessa o sistema da máquina
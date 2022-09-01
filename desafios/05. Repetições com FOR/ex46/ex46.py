from emoji import emojize
from time import sleep
# Falas iniciais
print('\033[33m='*10,'PREPARANDO PARA LANÇAR OS FOGOS','='*10,'\033[m')
sleep(0.7)
print(' '*15,'Vamos pra contagem')
sleep(0.7)
#Contagem regressiva
for i in range(10, -1, -1):
    print(' '*22,emojize('\033[31m:balloon:'),f'{i}\033[m')
    sleep(1)
#Explosões dos fogos
for i in range(5):
    print(' '*(2 + 5*i),emojize('\033[34m:collision:\033[m \033[34m:collision:\033[m \033[34m:collision:\033[m'))
    print(' '*(1 + 5*i),emojize('\033[34m:collision:\033[33m BOOM \033[34m:collision:\033[m'))
    print(' '*(2 + 5*i),emojize('\033[34m:collision:\033[m \033[34m:collision:\033[m \033[34m:collision:\033[m'))
    sleep(0.7)
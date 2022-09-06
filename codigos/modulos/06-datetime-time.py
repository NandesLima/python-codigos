from datetime import time  # Funções de manipulação de tempo

hora_atual = time(hour=6, minute=9, second=20, microsecond=22) # Cria um horário aleatório
hora_atual = time(hour=22, second=59).strftime('%H:%M') # Muda a formatação do horário e deixa o tipo como string
# %H --> hora
# %M --> minuto
# %S --> segundo

print(hora_atual)
from datetime import datetime # Módulo de manipulação de data e tempo

print(datetime.now()) # Retorna data e hora atual
print(datetime.now().strftime('%d/%m/%Y %H:%M:%S')) # Formata data e hora como se fosse uma string
# %H --> hora
# %M --> minuto
# %S --> segundo
# %d -> dia
# %m -> mês
# %y -> ano com 2 dígitos
# %Y -> ano com 4 dígitos

print(datetime.now().day) # Retorna apenas o dia atual
print(datetime.now().month) # Retorna apenas o mês atual
print(datetime.now().year) # Retorna apenas o ano atual
print(datetime.now().hour) # Retorna apenas a hora atual
print(datetime.now().minute) # Retorna apenas os minutos atuais
print(datetime.now().second) # Retorna apenas os segundos atuais
print(datetime.now().microsecond) # Retorna apenas os microssegundos atuais

print(datetime(day=27,month=7,year=1994,hour=20,minute=25,second=59)) # Cria uma data e hora
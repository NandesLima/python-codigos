from datetime import date  # Funções de manipulação de data

data_atual = date.today() # Retorna a data atual no padrão yyyy-mm-dd
ano_atual = date.today().year # Retorna o ano atual
dia_atual = date.today().day # Retorna o dia atual
mes_atual = date.today().month # Retorna o mês atual
data_atual = date.today().strftime('%d/%m/%Y') # Formata o tipo da data, o valor retornado é do tipo string
# %d -> dia
# %m -> mês
# %y -> ano com 2 dígitos
# %Y -> ano com 4 dígitos

print(data_atual)
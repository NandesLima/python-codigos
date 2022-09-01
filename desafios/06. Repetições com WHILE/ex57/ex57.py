from time import  sleep
while True:
    sexo = input('Digite o sexo (M/F): ').strip().upper()
    if sexo == 'M' or sexo == 'F':
        break
    else:
        print('Digite apenas M ou F')
        sleep(0.7)

if sexo == 'M':
    print('Masculino')
else:
    print('Feminino')
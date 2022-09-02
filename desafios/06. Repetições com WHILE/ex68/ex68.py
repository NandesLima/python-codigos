from time import sleep
from random import randint

count = 0
print('Vamos jogar par ou ímpar')
sleep(1)
while True:
    #Computador escolhe um valor entre 0 e 10
    print('Estou escolhendo um número entre 0 e 10')
    for i in range(50):
        print('.',end='')
        sleep(0.2)
    computador = randint(1,10)
    print('\nPronto, agora é sua vez')
    sleep(0.7)
    #Valida se o usuário está escolhendo entre 0 e 10
    while True:
        numero = int(input('Digite um número entre 0 e 10: '))
        if numero < 0 or numero > 10:
            print('Você só pode escolher um número entre 0 e 10')
            sleep(0.5)
        else:
            break
    #Soma o valor do usuário com o do computador
    numero += computador
    #Valida a escolha de par ou ímpar do usuário
    while True:
        escolha = input('Escolha P (Par) ou I (Ímpar): ').strip().upper()
        if escolha == 'P' or escolha == 'I':
            break
        else:
            print('Escolha apenas P ou I')
            sleep(0.5)
    #Verificando se a soma é par ou ímapar
    if numero %2 == 0:
        decisao = 'P'
    else:
        decisao = 'I'
    #Computador mostra os resultados
    print(f'O valor que eu escolhi foi {computador}, e a soma foi {numero}')
    if decisao == escolha:
        print(f'O resultado foi {decisao}, você venceu!!!')
        count += 1
    else:
        print(f'O resultado foi {decisao}, eu vencii!!!')
        break
print(f'Você venceu {count} partidas')
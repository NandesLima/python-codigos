extensos = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
            'onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito',
            'dezenove','vinte')

numero = 21
while numero < 0 or numero > 20:
    numero = int(input('Digite um número: '))
    if 0 <= numero <= 20:
        break
    print('Digite uma opção correta')
print(f'Número por extenso: {extensos[numero].capitalize()}')
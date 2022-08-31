print('SIMULAÇÃO DE EMPRÉSTIMOS')

casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário: R$ '))
prestacao_anual = int(input('Quantos anos de parcelas: '))

parcelas_mensais = prestacao_anual * 12
valor_mensal = (casa * 1.12)/parcelas_mensais

if valor_mensal > salario * 0.3:
    print('NEGADO: O valor da prestação passa de 30% do seu salário')
else:
    print(f'''APROVADO
    Você pagará {parcelas_mensais} parcelas de R$ {valor_mensal:.2f}
    Valor total: R$ {casa * 1.12:.2f}
    ''')

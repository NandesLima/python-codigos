salario = float(input('Digite o salário do funcionário: '))
if salario > 1250:
    print(f'Aumento de 10%, novo salário: R$ {salario * 1.1:.2f}')
else:
    print(f'Aumento de 15%, novo salário: R$ {salario * 1.15:.2f}')
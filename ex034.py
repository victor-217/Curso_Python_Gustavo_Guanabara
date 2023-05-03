"""EX034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.Para salários
superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%."""

salario = float(input('>>> Qual o valor do salário do funcionário? (R$)').replace('.', '').replace(',', ''))

if salario > 1250:

    aumento = (salario*10/100) + salario
    print(f'\n>> Com um aumento de 10% o funcionário que ganhava R${salario:.2f} passara a ganhar R${aumento:.2f}')

elif salario <= 1250:

    aumento = (salario*15/100) + salario
    print(f'\n>> Com um aumento de 15% o funcionário que ganhava R${salario:.2f} passará a ganhar R${aumento:.2f}')

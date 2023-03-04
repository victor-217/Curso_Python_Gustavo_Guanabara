"""EX013: Faça um algoritmo que leia o salário de um funcionário e mostre seu
novo salário, com 15% de aumento."""

salario = float(input('>>> Qual valor do salário do funcionário? R$'))

aumento = salario*15/100

print(f'\n>> Com aumento de 15%, o funcionário que ganhava R${salario} passará a ganhar R${salario+aumento:.2}')

'''
REAJUSTE SALARIAL: Faça um algoritmo que leia o salário de um funcionário e mostre
seu novo salário, com 15% de aumento
'''

sl = float(input('Qual valor do salário do funcionário? R$'))
aumento = sl + (sl*15 / 100)
print('\nO funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(sl, aumento))

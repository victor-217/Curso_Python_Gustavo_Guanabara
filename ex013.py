print('='*10, 'Ajuste Salarial', '='*10)

sl = float(input('Qual valor do salário do funcionário? R$'))
aumento = sl + (sl*15 / 100)
print('\nO funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(sl, aumento))

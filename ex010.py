'''
CONVERSOR DE MOEDAS: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos dólares ela pode comprar.
'''

real = float(input('Quanto você tem na carteira? (R$)'))
dl = real / 5.42
euro = real / 6.42
iene = real / 19.31
print('\nCom R${:.2f} você pode comprar US${:.2f}'.format(real, dl))
print('Com R${:.2f} você pode comprar €{:.2f}euros'.format(real, euro))
print('Com R${:.2f} você pode comprar ¥{:.2f}ienes'.format(real, iene))

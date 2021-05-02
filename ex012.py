'''
CALCULANDO DESCONTOS: Faça um algoritmo que leia o preço de um produto e mostre seu
novo preço, com 5% de desconto
'''

valor = float(input('Qual valor do produto? R$'))
desc = valor * 5 / 100
df = valor - desc
print('\nEste produto esta com desconto de 5%')
print('O produto que custava R${} na promoção vai custar R${:.2f}'.format(valor, df))

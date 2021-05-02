print('='*10, 'Loja Online', '='*10)

valor = float(input('Qual valor do produto? R$'))
desc = valor * 5 / 100
df = valor - desc
print('\nEste produto esta com desconto de 5%')
print('O produto que custava R${} na promoção vai custar R${:.2f}'.format(valor, df))

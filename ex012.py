"""EX012: Faça um algoritmo que leia o preço de um produto e mostre na tela seu
novo preço, com 5% de desconto."""

print('\033[95m========== LOJA ONLINE ==========\033[m')

valor = float(input('>>> Qual valor do produto? R$'))

desconto = (valor*5)/100

print('\n\033[32m>> VOCÊ GANHOU UM DESCONTO DE 5%!\033[m')
print(f'> Valor final a ser pago é de R${valor-desconto:.2f}')

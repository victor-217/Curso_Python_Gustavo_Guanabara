'''
ALUGUEL DE CARROS: Escreva um programa que pergunte a quantidade de km percorridos por
um carro alugado e a quantidade de dias pelo quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado
'''

dias = int(input('Quantos dias o carro ficou alugado? '))
Km = float(input('Quantos Km rodados? '))
pagar = (dias * 60) + (Km * 0.15)
print('\nO total a pagar é de R${:.2f}'.format(pagar))

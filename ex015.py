dias = int(input('Quantos dias o carro ficou alugado? '))
Km = float(input('Quantos Km rodados? '))
pagar = (dias * 60) + (Km * 0.15)
print('\nO total a pagar é de R${:.2f}'.format(pagar))

"""EX010: Crie um programa que leia quanto dinheiro a pessoa tem na carteira e
mostre quantos Dólares ela pode comprar."""

print('\033[95m====== CONVERSOR DE MOEDA ======\033[m')

real = float(input('Quanto você tem na carteira? (R$)'))

dl = real / 5.42
euro = real / 6.42
iene = real / 19.31

print(f'\nCom R${real:.2f} você pode comprar US${dl:.2f}')
print(f'Com R${real:.2f} você pode comprar €{euro:.2f}')
print(f'Com R${real:.2f} você pode comprar ¥{iene:.2f}')

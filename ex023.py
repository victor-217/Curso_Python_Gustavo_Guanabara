"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
ex:Digite um número:1111
unidade:
dezena:
centena:
milhar:
"""
num = input('Digite um número: ').zfill(4)
print('Analizando...')
print('\nUnidade: {}'.format(num[3]))
print('Dezena: {}'.format(num[2]))
print('Centena: {}'.format(num[1]))
print('Milhar: {}'.format(num[0]))

'''
DOBRO, TRIPLO, RAIZ QUDRADA:  Crie um programa que leia um número e mostre seu
dobro, triplo e raiz quadrada.
'''

from math import pow

num = int(input('Digite um número: '))
print('\nO dobro de {} vale {}'.format(num, num * 2))
print('O triplo de {} vale {}'.format(num, num * 3))
print('A raiz quadrada de {} é igual a {:.2f}'.format(num, pow(num, (1 / 2))))

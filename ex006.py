print('=' * 10, 'Dobro, Triplo e Raiz Quadrada', '=' * 10)

from math import pow

num = int(input('Digite um número: '))
print('\nO dobro de {} vale {}'.format(num, num * 2))
print('O triplo de {} vale {}'.format(num, num * 3))
print('A raiz quadrada de {} é igual a {:.2f}'.format(num, pow(num, (1 / 2))))

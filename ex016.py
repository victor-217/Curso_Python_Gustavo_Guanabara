'''
quebrando numero: Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porcao inteira
ex: digite um numero: 6.127 o número 6.127 tem a parte inteira 6
'''

from math import trunc

num = float(input('Digite um número: '))
print('O número digítado foi {} e sua porção inteira é {}'.format(num, trunc(num)))

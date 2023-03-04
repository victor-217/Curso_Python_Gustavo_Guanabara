"""EX016: Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porcao inteira
ex: digite um número: 6.127 o número 6.127 tem a parte inteira 6"""

from math import trunc

num = float(input('>>> Digite um número: '))

print(f'>> O número digítado foi {num} e sua parte inteira é {trunc(num)}.')
